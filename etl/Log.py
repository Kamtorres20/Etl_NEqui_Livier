import logging
from datetime import datetime
import pandas as pd

# Configurar el sistema de logs
def setup_logging():
    log_file = f"Files/Logs/program_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w"  # Sobrescribir el archivo cada vez que se ejecuta
    )
    logging.info("Sistema de logs configurado.")
    return log_file