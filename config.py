import os
# BD
HOST = "localhost"
USER = "postgres"
PASSWORD = "postgres"
DATABASE = "tesis_bomberos"

# Obtén el nombre de usuario actual
nombre_usuario = os.getlogin()

# CONFIG
PUNTO_PARTIDA = "-64.3451616313023,-33.12684997058952"
CIUDAD = "rio cuarto"
PROVINCIA = "cordoba"
PATH_REPORTE = f"/home/{nombre_usuario}/Descargas/reporte.txt"
SONIDO_ALARMA_INCENDIO_FORESTAL = f"/home/{nombre_usuario}/.local/share/QGIS/QGIS3/profiles/default/python/plugins/OnlineRoutingMapper/sonidos/iforestal.mp3"
SONIDO_ALARMA_INCENDIO_RURAL = f"/home/{nombre_usuario}/.local/share/QGIS/QGIS3/profiles/default/python/plugins/OnlineRoutingMapper/sonidos/irural.mp3"
SONIDO_ALARMA_INCENDIO_VEHICULAR = f"/home/{nombre_usuario}/.local/share/QGIS/QGIS3/profiles/default/python/plugins/OnlineRoutingMapper/sonidos/ivehicular.mp3"
SONIDO_ALARMA_RESCATE_ESTRUCTURA = f"/home/{nombre_usuario}/.local/share/QGIS/QGIS3/profiles/default/python/plugins/OnlineRoutingMapper/sonidos/iestructura.mp3"
SONIDO_ALARMA_ACCIDENTE_VEHICULAR = f"/home/{nombre_usuario}/.local/share/QGIS/QGIS3/profiles/default/python/plugins/OnlineRoutingMapper/sonidos/avehicular.mp3"
SONIDO_ALARMA_ACCIDENTE_MAT_PEL= f"/home/{nombre_usuario}/.local/share/QGIS/QGIS3/profiles/default/python/plugins/OnlineRoutingMapper/sonidos/matpel.mp3"
SONIDO_ALARMA_EMERGENCIAS_VARIAS = f"/home/{nombre_usuario}/.local/share/QGIS/QGIS3/profiles/default/python/plugins/OnlineRoutingMapper/sonidos/ivarios.mp3"
SONIDO_ALARMA_RESCATE_DE_ALTURA = f"/home/{nombre_usuario}/.local/share/QGIS/QGIS3/profiles/default/python/plugins/OnlineRoutingMapper/sonidos/raltura.mp3"
TIPO0 = "DESCONOCIDO"
TIPO1 = "INCENDIO FORESTAL"
TIPO2 = "INCENDIO RURAL"
TIPO3 = "INCENDIO VEHICULAR"
TIPO4 = "INCENDIO ESTRUCTURAL"
TIPO5 = "ACCIDENTE"
TIPO6 = "MATERIAL PELIGROSO"
TIPO7 = "VARIOS"
TIPO8 = "RESCATE DE ALTURA"

# TIPO AUTOMOVILES
CAMIONETA = "Camioneta"
CAMION_LIGERO = "Camion ligero"
CAMION_PESADO = "Camion pesado"


PATH_RUTA_EXPORT = f"/home/{nombre_usuario}/Descargas/archivo.ods"

# Tipos servicio
TIPO_SERVICIO_HERE_V8 = 7

# operadores
OPERADORES = [
    'Pedro',
    'Jose',
    'Ignacio'
]

# tipos Emergencia
TIPOS_EMERGENCIA = [
    'Todos',
    'Incendio forestal',
    'Incendio rural',
    'Incendio vehicular',
    'Incendio estructural',
    'Accidente',
    'Material peligroso',
    'Rescate altura',
    'Varios'
]

FILTRAR_EMERGENCIA = 0
GRAFICOS_BARRA = 1
GRAFICOS_LINEA = 2