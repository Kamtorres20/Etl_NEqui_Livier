from .config import get_redshift_connection

def load_to_redshift(bucket_name,s3_file_path,table):
    """Carga un DataFrame a una tabla de Redshift."""

    iam_role = ""  # Rol IAM con acceso a S3
    s3_path = f"s3://{bucket_name}/{s3_file_path}"

    truncate_query = f"""TRUNCATE TABLE {table};"""
    

    copy_query = f"""
    COPY {table}
    FROM '{s3_path}'
    IAM_ROLE '{iam_role}'
    DELIMITER ','
    IGNOREHEADER 1
    REGION 'us-east-1'
    CSV;
    """
    try:
        conn = get_redshift_connection()
        cursor = conn.cursor()
        cursor.execute(truncate_query)
        cursor.execute(copy_query)
        conn.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al conectar a Redshift: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        
       
