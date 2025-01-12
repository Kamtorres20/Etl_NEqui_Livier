# Proyecto ETL: S3 a Redshift

Este proyecto implementa un proceso ETL (Extract, Transform, Load) que toma datos en formato JSON almacenados en un bucket de Amazon S3, los transforma según reglas definidas, y los carga en una tabla de Amazon Redshift.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
- [Pruebas](#pruebas)
- [Personalización](#personalización)
- [Contribuciones](#contribuciones)

---

## Requisitos

- **Python 3.8 o superior**
- **Amazon S3:** Un bucket configurado con un archivo JSON de entrada.
- **Amazon Redshift:** Una tabla creada para almacenar los datos procesados.
- Las siguientes bibliotecas de Python:
  - `boto3`
  - `pandas`
  - `psycopg2`

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Kamtorres20/Etl_NEqui_Livier.git
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura tus credenciales de AWS y Redshift en `etl/config.py`:
   ```python
   # Configuración de AWS
   AWS_ACCESS_KEY = 'tu_access_key'
   AWS_SECRET_KEY = 'tu_secret_key'
   REGION_NAME = 'tu_region'

   # Configuración de Redshift
   REDSHIFT_HOST = 'tu_redshift_host'
   REDSHIFT_PORT = 5439
   REDSHIFT_DB = 'tu_base_de_datos'
   REDSHIFT_USER = 'tu_usuario'
   REDSHIFT_PASSWORD = 'tu_contraseña'
   ```

4. Configura tu tabla de Redshift:
   ```sql
   CREATE TABLE carritos (
      cart_id INTEGER PRIMARY KEY,
      user_id INTEGER REFERENCES usuarios(user_id),
      total DECIMAL(10,2) NOT NULL,
      discounted_total DECIMAL(10,2),
      total_products INTEGER,
      total_quantity INTEGER
   );

   CREATE TABLE productos (
    product_id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    thumbnail VARCHAR(255)
   );

   CREATE TABLE carritos_productos (
    cart_id INTEGER REFERENCES carritos(cart_id),
    product_id INTEGER REFERENCES productos(product_id),
    quantity INTEGER,
    total DECIMAL(10,2),
    discounted_total DECIMAL(10,2),
    PRIMARY KEY (cart_id, product_id)
   );

   ```

---

## Estructura del Proyecto

```plaintext
etl_project/
├── etl/                      # Código principal del ETL
│   ├── config.py             # Configuración de AWS y Redshift
│   ├── log.py                # Configuración de log interno
│   ├── s3_utils.py           # Funciones para interactuar con S3
│   ├── transform.py          # Lógica de transformación de datos
│   ├── redshift_utils.py     # Funciones para interactuar con Redshift
├── tests/                    # Pruebas unitarias
│   ├── test_etl.py           # Pruebas del proceso ETL
├── main.py                   # Script principal del ETL
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto
```

---

## Uso

1. Ejecuta el proceso ETL:
   ```bash
   python scripts/main.py
   ```

2. Personaliza los parámetros de entrada y salida modificando estas variables en `main.py`:
   ```python
   BUCKET_NAME = 'tu_bucket_name'
   INPUT_KEY = 'ruta_al_archivo.json'
   REDSHIFT_TABLE = 'tu_tabla_redshift'
   ```

---

## Pruebas

Para ejecutar las pruebas unitarias, utiliza el siguiente comando:
```bash
python -m unittest discover tests
```

Esto ejecutará todas las pruebas en la carpeta `tests/` y mostrará los resultados.

---

## Personalización

- **Transformación de datos:**
  La lógica de transformación está definida en `etl/transform.py`. Puedes modificar la función `transform` para adaptarla a tus necesidades específicas.

- **Configuración de S3:**
  La configuración de las credenciales y el cliente S3 se encuentra en `etl/config.py`.

- **Configuración de Redshift:**
  La conexión a Redshift también se define en `etl/config.py`. Asegúrate de que los nombres de las columnas coincidan con la tabla Redshift.


