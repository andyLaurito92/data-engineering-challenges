import requests
from medicalpublications.libraries.fileUploader import S3FileUploader

def read_all():
    base_url = "https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/"
    bucket_name = "sources-medical-publications"

    ## TODO: Investigate better way to do this :)
    result = requests.get(base_url)
    files = [x.group(2) for x in re.finditer("(<a.*>)(.*.xml.gz)(</a>)",output.text)]
    dates = [x.group(2).strip().replace("-", "/") for x in re.finditer("(</a>)(.*\d+\-\d+\-\d+)",output.text)]

    files_to_download = 2
    i = 0
    for file, date in zip(files, dates):
        result = requests.get(base_url + file)
        ## TODO: Add check that validates that size is always under lambda maximum
        S3FileUploader.upload_bytes("{}/{}".format(date,file), result.content, bucket_name)
        print("File uploaded!")
        i += 1
        if files_to_download == i:
            return

