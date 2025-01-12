# Diagrama de Flujo Simplificado para la Limpieza de Datos

             [Inicio]
                 |
         -------------------
         |                 |
[Carga de Datos]       [Configurar Logs]
         |                 |
         -------------------
                 |
         [Identificar Problemas]
                 |
   ----------------------------------
   |                                |
[Duplicados Detectados?]  [Formato Incorrecto?]
         |                                |
[Eliminar Duplicados]            [Corregir Formatos]
         |                                |
        ----------------------------------
                 |
         [Validar Consistencia]
                 |
     -----------------------------
     |                           |
[Valores Nulos Detectados?]  [Consistentes]
         |                           |
  [Eliminar/Llenar Nulos]     [Guardar Datos Limpios]
                 |
              [Fin]
