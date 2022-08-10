#!/usr/bin/env bash
set -x
awslocal s3 mb s3://sources-medical-publications
awslocal s3 mb s3://uncompressed-medical-publications
awslocal s3 mb s3://output-medical-publications
set +x
