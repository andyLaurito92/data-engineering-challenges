keyword=$1
zgrep -i -m 1 $keyword pubmed22n1115.xml.gz
# rg -q keyword pubmed22n1115.xml --> this returns an exit code; Read it using echo $?
