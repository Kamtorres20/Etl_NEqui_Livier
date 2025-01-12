import boto3
import psycopg2
from sqlalchemy import create_engine

# Configuración de AWS 
AWS_ACCESS_KEY = 'WD'
AWS_SECRET_KEY = ''
REGION_NAME = 'us-east-1'

# Configuración de Redshift
REDSHIFT_HOST = ''
REDSHIFT_PORT = 5439
REDSHIFT_DB = ''
REDSHIFT_USER = ''
REDSHIFT_PASSWORD = ''

def get_s3_client():
    """Devuelve un cliente de S3 con la configuración especificada."""
    return boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=REGION_NAME
    )

def get_redshift_connection():
    """Devuelve una conexión a Redshift."""
    connection = psycopg2.connect(
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT,
        dbname=REDSHIFT_DB,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD
    )    
    
    return connection








