import logging
from etl.s3_utils import read_json_from_s3,Load_csv_to_s3
from etl.transform import transform,SaveCSV
from etl.redshift_utils import load_to_redshift
from etl.Log import setup_logging




# Parámetros
BUCKET_NAME = 'mybucketnequi'
INPUT_KEY = 'Source/carts.json'
OUTPUT_KEY= 'DataTransform/carritos.csv'
OUTPUT_KEY_PRODUCTS= 'DataTransform/Productos.csv'
OUTPUT_KEY_CARS_PRODUCTS= 'DataTransform/Carrito_Productos.csv'
REDSHIFT_TABLE = 'carritos'
REDSHIFT_TABLE_PRODUCTOS = 'productos'
REDSHIFT_TABLE_CARRITOS_PRODUCTOS = 'carritos_productos'

def run_etl():

    log_file = setup_logging()

    # Extraer
    logging.info("Iniciando extracción...")
    raw_data = read_json_from_s3(BUCKET_NAME, INPUT_KEY)
    logging.info("Extracción completada.")


    # Transformar
    logging.info("Iniciando transformación...")
    transformed_data,transformed_data_Products,transformed_data_Car_Products = transform(raw_data)  
    logging.info("Guardado CSV Local...")  
    csv_file,csv_file_prod,csv_file_Car_prod = SaveCSV(transformed_data,transformed_data_Products,transformed_data_Car_Products)
    logging.info("cargando CSV en S3")  
    Load_csv_to_s3(csv_file,BUCKET_NAME,OUTPUT_KEY)
    Load_csv_to_s3(csv_file_prod,BUCKET_NAME,OUTPUT_KEY_PRODUCTS)
    Load_csv_to_s3(csv_file_Car_prod,BUCKET_NAME,OUTPUT_KEY_CARS_PRODUCTS)
    logging.info("Transformación completada.")      

    # Cargar
    logging.info("Iniciando carga...")     
    load_to_redshift(BUCKET_NAME, OUTPUT_KEY,REDSHIFT_TABLE)
    load_to_redshift(BUCKET_NAME, OUTPUT_KEY_PRODUCTS,REDSHIFT_TABLE_PRODUCTOS)
    load_to_redshift(BUCKET_NAME, OUTPUT_KEY_CARS_PRODUCTS,REDSHIFT_TABLE_CARRITOS_PRODUCTOS)
    logging.info("Carga completada.") 
    


if __name__ == "__main__":
    run_etl()
