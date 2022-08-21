from lxml import etree

doc = etree.parse("/Users/andylaurito/Desktop/data-engineering/data-engineering-challenge/bayer-challenge/pubmed22n1115.xml")
for pubmed_article in doc.xpath("//PubmedArticle"):
    pubmed_article_xml = etree.tostring(pubmed_article, pretty_print=True)
    pubmed_id = pubmed_article.xpath("MedlineCitation/PMID/text()")[0]
    with open("./pubmed_article_{}.xml".format(pubmed_id), "wb") as f:
        f.write(pubmed_article_xml)
 
