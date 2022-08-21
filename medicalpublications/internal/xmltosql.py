## Uplaods the xml into postgres
#from urllib.request import urlopen, Request
import pandas as pd
from lxml import etree

## Convert xml into data that can be uploaded to sql
base_url = "http://localhost:4566/uncompressed-medical-publications/"
example_file = "pubmed22n1115.xml"
date = "2021/12/13/"

## Write pubmed xml into sql
pubmed_article = etree.parse("/Users/andylaurito/Desktop/data-engineering/data-engineering-challenge/bayer-challenge/pubmedArticle.xml")

pubmed_columns=[
    "PMID",
#    "DateCompleted",
#    "DateRevised",
    "ArticleTitle",
    "Language",
    "Author",
    "Chemical",
    "Abstract"
]

## Columns pick up arbitarly
#date_completed = pubmed_article.xpath("//{}/*/text()".format(pubmed_columns[0]))
#date_revised = pubmed_article.xpath("//{}/*/text()".format(pubmed_columns[1]))
pmid = pubmed_article.xpath("//{}/text()".format(pubmed_columns[0]))[0]
article_title = pubmed_article.xpath("//{}/text()".format(pubmed_columns[1]))[0]
language = pubmed_article.xpath("//{}/text()".format(pubmed_columns[2]))[0]
authors = []
for auth in pubmed_article.xpath("//{}".format(pubmed_columns[3])):
    last_name_xpath = auth.xpath("LastName/text()")
    fore_name_xpath = auth.xpath("ForeName/text()")
    fore_name = ""
    last_name = ""
    if len(last_name_xpath) != 0:
        last_name = last_name_xpath[0]
    else:
        print("last name was empty")

    if len(fore_name_xpath) != 0:
        fore_name = fore_name_xpath[0]
    else:
        print("fore name was empty")

    authors.append("{} {}".format(fore_name, last_name))

chemicals = []
for chemical in pubmed_article.xpath("//{}".format(pubmed_columns[4])):
    registry_number = chemical.xpath("RegistryNumber/text()")[0]
    substance = chemical.xpath("NameOfSubstance/text()")[0]
    chemicals.append("{} : {}".format(registry_number, substance))

abstract = ""
abstract_xpath = pubmed_article.xpath("//{}/*/text()".format(pubmed_columns[5]))
if len(abstract_xpath) != 0:
    abstract = abstract_xpath[0]

row_pubmed = [pmid, article_title, language, abstract]
row_authors = names
row_chemicals = chemicals

df = pd.DataFrame([row_pubmed], columns=["PMID", "Title", "Language", "Abstract"])
## From now on, we can define our diemnsions
