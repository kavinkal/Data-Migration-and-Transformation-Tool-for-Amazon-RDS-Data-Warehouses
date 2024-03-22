# Data-Migration-and-Transformation-Tool-for-Amazon-RDS-Data-Warehouses
This Project is all about downloading the zip file from the URL and extracting the data to store in json file in s3 then, transform the data to load in RDS.

Problem Statement:

The objective is to utilize the request method to download the zip file from the provided URL, extract its contents, and subsequently upload the data to AWS S3. Following this, a Lambda function will be employed to trigger the data to be stored in the database.

Technology Stack Used

• Python

• AWS S3

• AWS RDS

• AWS IAM

REQUIRED LIBRARIES:

requests
zipfile
boto3
Json
Approach

To begin, utilize the request library to download the JSON ZIP file from the specified URL. Then, employ the zipfile module, along with its limit method, to extract the data from the downloaded ZIP file.

Proceed by creating an S3 bucket and generating a new IAM policy to grant permissions for AWS S3, Lambda, and CloudWatch to read and write data.

Next, establish a table in RDS and load the data after tranforming the data. making the data into tabular format using pandas and loading the data into RDS

Using AWS IAM, generate access and secret keys to connect AWS S3 locally via the boto3 method. With boto3, upload the downloaded JSON files to the S3 bucket.


