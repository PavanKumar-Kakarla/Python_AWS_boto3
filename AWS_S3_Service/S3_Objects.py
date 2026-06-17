import boto3

# Define the region explicitly
REGION = "ap-south-1"

# Create an Object for S3 Service using Client
s3_client = boto3.client("s3", region_name=REGION)
print("S3_Client:", s3_client)

# Upload the object into S3 Bucket
def upload_object():
    try:
        s3_client.upload_file(
            Filename=r"D:\test.txt",
            Bucket="pavan-boto3-demo-2026",
            Key="test.txt"
        )
        print("File Uploaded Successfully")
    except Exception as e:
        print("Uploading Object into S3 Bucket Failed:", str(e))


# Download the Object from S3 Bucket
def download_object():
    try:
        s3_client.download_file(
            "pavan-boto3-demo-2026",
            "test.txt",
            r"D:\download-test.txt"
        )
        print("File Downloaded Successfully")
    except Exception as e:
        print("Downloading S3 Objects Failed", str(e))


# Copy the Object
def copy_object():
    try:
        copy_source = {
            "Bucket": "pavan-boto3-demo-2026",
            "Key": "test.txt"
        }

        s3_client.copy_object(
            CopySource=copy_source,
            Bucket="pavan-boto3-demo-2026",
            Key="test-renamed.txt"
        )
        print("Object Copied Successfully")
    except Exception as e:
        print("Copying S3 Objects Failed", str(e))

# Delete the Object
def delete_object():
    try:
        s3_client.delete_object(
            Bucket="pavan-boto3-demo-2026",
            Key="test.txt"
        )
        print("Object Deleted Successfully")
    except Exception as e:
        print("Deleting S3 Object Failed", str(e))

# Head Object(Meta Data)
def meta_data():
    try:
        response = s3_client.head_object(
            Bucket="pavan-boto3-demo-2026",
            Key="test-renamed.txt"
        )

        print("Content Length:", response["ContentLength"])
        print("Content Type:", response["ContentType"])
        print("ETag:", response["ETag"])
        print("Version ID:", response.get("VersionId"))
        print("Last Modified:", response["LastModified"])
        print("Encryption:", response.get("ServerSideEncryption"))

    except Exception as e:
        print("S3 Object Meta Data Failed", str(e))


#List of objects in S3 Bucket
def list_objects():
    try:
        response = s3_client.list_objects_v2(
            Bucket="pavan-boto3-demo-2026"
        )
        for obj in response["Contents"]:
            print("Key :", obj["Key"])
            print("Size:", obj["Size"])
            print("Last Modified:", obj["LastModified"])
            print("-" * 40)
    except Exception as e:
        print("S3 Objects List Failed", str(e))


# upload_object()
# download_object()
# copy_object()
# delete_object()
# meta_data()
list_objects()