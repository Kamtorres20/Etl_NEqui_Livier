import unittest
import psycopg2
from psycopg2 import OperationalError

class TestRedshiftConnection(unittest.TestCase):
    # Configuración de conexión
    HOST = ''
    PORT = 5439
    DBNAME = ''
    USER = ''
    PASSWORD = ''

    def test_redshift_connection(self):
        """Test para validar la conexión a Redshift"""
        try:
            # Intentar establecer la conexión
            connection = psycopg2.connect(
                host=self.HOST,
                port=self.PORT,
                dbname=self.DBNAME,
                user=self.USER,
                password=self.PASSWORD
            )
            # Verificar que la conexión se establece correctamente
            self.assertIsNotNone(connection, "La conexión a Redshift no se pudo establecer.")
            
            # Cerrar la conexión después del test
            connection.close()
        except OperationalError as e:
            self.fail(f"No se pudo conectar a Redshift: {e}")

if __name__ == '__main__':
    unittest.main()
