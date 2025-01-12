import unittest
from etl.transform import transform

class TestETL(unittest.TestCase):
    def test_transform(self):
        # Datos de prueba
        input_data = [
            {"columna1": 1, "columna2": 2},
            {"columna1": 3, "columna2": 4},
        ]
        # Llamar a la función de transformación
        result = transform(input_data)
        # Verificar que las columnas y valores sean correctos
        self.assertEqual(list(result.columns), ["columna1", "columna2", "nueva_columna"])
        self.assertEqual(result["nueva_columna"].tolist(), [2, 6])

if __name__ == "__main__":
    unittest.main()