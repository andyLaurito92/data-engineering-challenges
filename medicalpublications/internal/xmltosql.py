## Uplaods the xml into postgres
from urllib.request import urlopen, Request
import pandas as pd
import xml.etree.ElementTree as ET
#from lxml import etree
import psycopg2

## Convert xml into data that can be uploaded to sql
def insert_xml_into_postgress():
    base_url = "http://localhost:4566/uncompressed-medical-publications/"
    example_file = "pubmed22n1115.xml"
    date = "2021/12/13/"

    ## Read xml
    #result = requests.get(base_url + date + example_file) 
    #xml = result.content

    ## Create psql connection
    # conn_string = ("host=host dbname=lal user=user password=pass")
    # conn = psycopg2.connect(conn_string)
    # cursor = conn.cursor()

    ## Write xml into sql
    tree = ET.parse(xml)
    root = tree.getroot()
    for pubmed_article in root.iter("PubmedArticle"):
        pubmed_data = pubmed_article.find("PubmedData")

        ## Nodes under pubmed data
        history = pubmed_data.find("History")
        publicationStatus = pubmed_data.find("PublicationStatus")
        articleIdList = pubmed_data.find("ArticleIdList")
        referenceList = pubmed_data.find("ReferenceList")

        ## Nodes under medline citation
        medline_citation = pubmed_article.find("MedlineCitation")
        pmid = medline_citation.find("PMID")
        date_completed = medline_citation.find("DateCompleted")
        date_revised = medline_citation.find("DateRevised")
        article = medline_citation.find("Article")
        medline_journal_info = medline_citation.find("MedlineJournalInfo")
        chemical_list = medline_citation.find("ChemicalList")
        citation_subset = medline_citation.find("CitationSubset")
        meshHeading_list = medline_citation.find("MeshHeadingList")
        keyword_list = medline_citation.find("KeywordList")
        coi_statement = medline_citation.find("CoiStatement")


        dfs_data = []
        for node in [history, publicationStatus, articleIdList, referenceList]:
            dfs_data.append(pd.read_xml(ET.tostring(node)))
        
        for elem in pubmed_data:
            print(elem)
        
        for elem in pubmed_data:
            print(elem)
        return
        #postgres = ('INSERT INTO epg_live (channel_id, program, start, duration) VALUES (%s, %s, %s, %s)', (row, row, row, row))
        #cursor.execute(parser,postgres)
        #cursor.commit()
        #print "Gotovo!"

