#Download the zipfile using url
#extract the zipfile and store it in local
#move to s3

#data we are fetching from s3 and performed data transform
#Finally, Migrate the data to RDS


import json
import boto3
import pandas as pd

s3_client = boto3.client('s3')
bucket_name = 's3bucketguvi'
data_list = []

# List all objects in the bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)

# Iterate over each object in the bucket
for obj in response['Contents']:
    key = obj['Key']
    
    # Retrieve the object from S3
    s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)
    
    # Load JSON data from the object's content
    data = json.loads(s3_object['Body'].read().decode('utf-8'))
    
    # Append loaded data to the list
    data_list.append(data)

# Function to modify the loaded data
def data_modification(data_list):
    flatten_data = []
    
    # Iterate over each loaded data
    for data in data_list:
        taxonomy = data['facts'].keys()
        
        # Iterate over taxonomy in the data
        for tax in taxonomy:
            standard = data['facts'][tax].keys()
            
            # Iterate over standards in the taxonomy
            for std in standard:
                su = list(data['facts'][tax][std]['units'].keys())
                
                # Iterate over items in the units
                for item in data['facts'][tax][std]['units'][su[0]]:
                    row = {
                        'cik': data['cik'],
                        'EntityName': data['entityName'],
                        'Taxonomy': tax,
                        'Units':su[0],
                        'Standard': std,
                        'Start': item.get('start'),
                        'end': item['end'],
                        'val': item['val'],
                        'accn': item['accn'],
                        'fy': item['fy'],
                        'fp': item['fp'],
                        'form': item['form'],
                        'filed': item['filed'],
                        'frame': item.get('frame')
                    }
                    flatten_data.append(row)
        
    df = pd.DataFrame(flatten_data)
    return df

# Modify the loaded data
extracted_data = data_modification(data_list)


