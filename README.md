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
- [Licencia](#licencia)

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
   CREATE TABLE sales_data (
      id INT,                           -- Identificador único de la venta
      total NUMERIC(10, 2),             -- Total sin descuentos
      discounted_total NUMERIC(10, 2),  -- Total con descuentos aplicados
      user_id INT,                      -- Identificador del usuario que realizó la compra
      total_products INT,               -- Número total de productos distintos en la venta
      total_quantity INT                -- Cantidad total de productos comprados
   );
   ```

---

## Estructura del Proyecto

```plaintext
etl_project/
├── etl/                      # Código principal del ETL
│   ├── __init__.py           # Archivo para tratar la carpeta como un módulo
│   ├── config.py             # Configuración de AWS y Redshift
│   ├── s3_utils.py           # Funciones para interactuar con S3
│   ├── transform.py          # Lógica de transformación de datos
│   ├── redshift_utils.py     # Funciones para interactuar con Redshift
├── scripts/                  # Scripts ejecutables
│   ├── main.py               # Script principal del ETL
├── tests/                    # Pruebas unitarias
│   ├── test_etl.py           # Pruebas del proceso ETL
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto
```

---

## Uso

1. Ejecuta el proceso ETL:
   ```bash
   python scripts/main.py
   ```

2. Personaliza los parámetros de entrada y salida modificando estas variables en `scripts/main.py`:
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


