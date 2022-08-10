## Consuming from the National Center for Biotechnology Information

## What I'll be doing?

In this project I'll be consuming data from [this](https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/) ftp in order to make it available for data scientists as a unique downloadable file. I will also impelemnt the support of querying data by specific keywords and timeframes.

If you get into the mentioned link, you will see that each date 3 files are uploaded:

1. pubmed22n1141.xml.gz 
2. pubmed22n1141.xml.gz.md5
3. pubmed22n1141_stats.html

The first file contains information related to medical publications which is compressed using gz, the second file contains the md5 hash and the last file seems to contain metadata related to how many entries were either added, removed or revisited (updated?)



### Goals

1. To make the data downloadble as a whole
2. To make data queryable for a specific keyword (for example "TP53") and a given frame (Pubdate)

## Implementation details

This repo is using localstack, so you can run (to be changed in the future) the python scripts manually and you will be writing to your local s3 buckets

In order to spin-up locakstack, run `docker-compose up`




