#taking the data to extract 

import zipfile
import os
import boto3
import json

# store the json extract file locally
def extract_zip(zip_file_path, extract_to):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        file_list=zip_ref.namelist()
        for file in file_list:
            zip_ref.extractall(extract_to)
    print("Successfully extracted.")


zip_file_path = r"C:\Users\kumar\OneDrive\Desktop\Project\company.zip"  
extract_to = r"C:\Users\kumar\OneDrive\Desktop\Project\data_pratice"

os.makedirs(extract_to, exist_ok=True)

# Extract the zip file
extract_zip(zip_file_path, extract_to)

#move the file to s3 bucket

#extract_to = r"C:\Users\kumar\OneDrive\Desktop\Project\data_pratice"

# Step 3: Parse the JSON Data and Store in Amazon S3
s3 = boto3.client('s3')
bucket_name = 's3bucketguvi'
for file_name in os.listdir(extract_to):
    if file_name.endswith('.json'):
        with open(os.path.join(extract_to, file_name), 'r') as f:
            data = json.load(f)
        s3.upload_file(os.path.join(extract_to, file_name), bucket_name, file_name)