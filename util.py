
import requests
from .db import insert,select
from uu import decode
from urllib.request import urlopen
import json
import re
from .config import *

def geocode_address(address):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            # Extrae las coordenadas (latitud y longitud) del primer resultado
            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            return lon, lat
    return None

def report(url):
    response = urlopen(url).read().decode("utf-8")
    diccionario = json.loads(response)
    f = open (PATH_REPORTE,'a')
    for route in diccionario['response']['route']:
        f.write(re.sub(r"\<[^>]*\>", "",(route['summary']['text']))+'\n\n')
        for leg in route['leg']:
            for maneuver in leg['maneuver']:
                f.write(re.sub(r"\<[^>]*\>", "",(maneuver['instruction']))+'\n')
    registros = select('points')
    if (len(registros) > 0) :
        f.write('\nCortes\n')
        for x in range(0,len(registros),2):
            f.write(str(registros[x][3]))
    f.close()

def obtener_direccion(latitud, longitud):
    url = f"https://nominatim.openstreetmap.org/search?format=json&lat={latitud}&lon={longitud}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            direccion = data[0]["display_name"]
            return direccion
        else:
            return "No se encontró ninguna dirección para las coordenadas proporcionadas."
    else:
        return f"Error al realizar la solicitud: {response.status_code}"
    
def agregar_texto_con_saltos_de_linea(c, x, y, texto):
    lineas = texto.split('\n')
    for linea in lineas:
        c.drawString(x, y, linea)
        y -= 15  # Espacio vertical entre líneas


def insertar_punto(start_point, stop_point, description):
    valores = "{}, {}, '{}'".format(start_point, stop_point, description)
    insert('points', 'startPoint, stopPoint, description', valores)
