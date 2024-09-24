import boto3

def list_s3_objects(bucket_name):
    # Create an S3 client
    s3_client = boto3.client('s3')

    # List objects in the specified bucket
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        # Check if the bucket is not empty
        if 'Contents' in response:
            print("Objects in bucket:")
            for obj in response['Contents']:
                print(f" - {obj['Key']} (Size: {obj['Size']} bytes)")
        else:
            print("The bucket is empty.")
    
    except Exception as e:
        print(f"Error: {e}")

# Replace 'your-bucket-name' with your actual bucket name
list_s3_objects('aws-teja-project')
