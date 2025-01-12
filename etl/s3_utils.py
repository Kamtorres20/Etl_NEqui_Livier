import json
from .config import get_s3_client

def read_json_from_s3(bucket_name, file_key):
    """Lee un archivo JSON desde un bucket de S3."""
    s3_client = get_s3_client()
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    data = response['Body'].read().decode('utf-8')
    return json.loads(data)

def Load_csv_to_s3(csv_file,bucket_name,s3_file_path):
    s3_client = get_s3_client()
    s3_client.upload_file(csv_file, bucket_name, s3_file_path)
    print(f"Archivo subido exitosamente a s3://{bucket_name}/{s3_file_path}")
