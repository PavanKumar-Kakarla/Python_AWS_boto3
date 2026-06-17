import boto3

# Define the region explicitly
REGION = "ap-south-1"
BUCKET_NAME = "pavan-boto3-demo-2026"

# Create an Object for S3 Service using Client
s3_client = boto3.client("s3", region_name=REGION)
print("S3_Client:", s3_client)

# Creating the S3 Bucket with the required LocationConstraint for Mumbai
"""When creating a bucket outside the default us-east-1 region, AWS requires the LocationConstraint parameter 
to specify the target region where the bucket should be created."""

def create_bucket():
    try:
        response = s3_client.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={
                'LocationConstraint': REGION
            }
        )
        print("Bucket created Successfully:", response)
    except Exception as e:
        print("Creating Bucket Failed", str(e))


# Delete Bucket
def delete_bucket():
    try:
        s3_client.delete_bucket(
            Bucket=BUCKET_NAME
        )
        print("Bucket deleted successfully")
    except Exception as e:
        print("Deleting Bucket Failed", str(e))

# List Buckets
def list_buckets():
    try:
        buckets_list = s3_client.list_buckets()
        for bucket in buckets_list["Buckets"]:
            print("Bucket Name : ",bucket["Name"])
            print("Bucket Created On : ", bucket["CreationDate"])
    except Exception as e:
        print("Retriving Buckets Failed", str(e))


#create_bucket()
#delete_bucket()
list_buckets()
