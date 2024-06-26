import psycopg2
from psycopg2 import sql
from .config import *
import datetime
                
def connectBD():
    # Conectar a la base de datos
    conexion = psycopg2.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = DATABASE
    )
    return conexion

def createTablePoints():
    conexion = connectBD()
    cursor = conexion.cursor()

    # Crear una tabla si no existe
    consulta_creacion_tabla = """
        CREATE TABLE IF NOT EXISTS points (
            id SERIAL PRIMARY KEY,
            startPoint VARCHAR(40),
            stopPoint VARCHAR(40),
            description VARCHAR(255)
        )
    """
    cursor.execute(consulta_creacion_tabla)

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()


def insert(table = '', columns = '', values = ''):
    if table != '' and columns != '' and values != '':
        conexion = connectBD()
        cursor = conexion.cursor()
        consulta_insercion = sql.SQL("INSERT INTO {} ({}) VALUES ({})".format(table, columns, values))
        cursor.execute(consulta_insercion)

        # Guardar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close()


def select(table = '', id = None, limit = None, filtro = {}):
    if (table == ''):
        return []
    
    conexion = connectBD()
    cursor = conexion.cursor()
    query = "SELECT * FROM {} WHERE 1 = 1 ".format(table)
    
    if (id is not None):
        query+= " AND id = {} ".format(id)

    if 'fecha_desde' in filtro:
        query += " AND fecha >= '{}'".format(filtro['fecha_desde'])

    if 'fecha_hasta' in filtro:
        query += " AND fecha <= '{}'".format(filtro['fecha_hasta'])

    if 'tipo_emergencia' in filtro:
        query += " AND tipo = '{}'".format(filtro['tipo_emergencia'])
    
    if 'hours' in filtro:
        query+= " AND EXTRACT(HOUR FROM fecha) = '{}'".format(filtro['hours'])

    query += "ORDER BY id"

    if (limit is not None):
        query+= " DESC LIMIT {}".format(limit)
    
    cursor.execute(query)
    result = cursor.fetchall()
    conexion.close()

    return result[0] if id is not None else result

def delete(table = '', id = None):
    if (table != ''):
        conexion = connectBD()
        cursor = conexion.cursor()
        query = "DELETE FROM {} WHERE 1 = 1".format(table)
        
        if (id is not None):
            query+= " AND id = {}".format(id)
        
        cursor.execute(sql.SQL(query))
        conexion.commit()
        conexion.close()

def update(table = '', seters = '', id = None):
    if (table != '' and seters != ''):
        conexion = connectBD()
        cursor = conexion.cursor()
        query = "UPDATE {} SET {} WHERE 1 = 1 AND id = {} ;".format(table,seters,id)

        cursor.execute(sql.SQL(query))
        conexion.commit()
        conexion.close()

def update_file(table = '',nombre='', contenido = '', id = None):
    if (table != '' and contenido != ''):
        conexion = connectBD()
        cursor = conexion.cursor()
        
        # Prepara la consulta SQL con un parámetro para el contenido binario
        query = sql.SQL("UPDATE archivo SET nombre_archivo = %s, contenido = %s WHERE id = %s")
    
        # Ejecuta la consulta SQL pasando los datos binarios como parámetros
        cursor.execute(query, (nombre, psycopg2.Binary(contenido), id))
        
        conexion.commit()
        conexion.close()




#tabla para tener registro de las bombas de aguas que pueden ser utilizadas en un incendio
def createTableBomba():
    conexion = connectBD()
    cursor = conexion.cursor()

    # Crear una tabla si no existe
    consulta_creacion_tabla_bomba = """
        CREATE TABLE IF NOT EXISTS bomba (
            id SERIAL PRIMARY KEY,
            startPoint VARCHAR(40),
            stopPoint VARCHAR(40),
            description VARCHAR(255),
            estado CHAR(1) CHECK (estado IN ('I', 'A')) DEFAULT 'A'
        )
    """
    cursor.execute(consulta_creacion_tabla_bomba)

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()


def insertarBomba(startPoint,stopPoint, description=""):
    conexion = connectBD()
    cursor = conexion.cursor()

    consulta_insercion_bomba = sql.SQL("INSERT INTO bomba (startpoint, stoppoint, description) VALUES (%s, %s, %s)")
    datos_bomba = (startPoint, stopPoint, description)
    cursor.execute(consulta_insercion_bomba, datos_bomba)


    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()


def seleccionarBomba():
    conexion = connectBD()
    cursor = conexion.cursor()

    consulta_seleccion_bomba = "SELECT * FROM bomba"

    cursor.execute(consulta_seleccion_bomba)

    resultados = cursor.fetchall()
    conexion.close()

    return resultados

def seleccionarBomba(id):
    conexion = connectBD()
    cursor = conexion.cursor()

    consulta_seleccion_bomba = "SELECT * FROM bomba WHERE id = {}".format(id)

    cursor.execute(consulta_seleccion_bomba)

    resultado = cursor.fetchall()
    conexion.close()
    
    return resultado[0]

def borrarBomba(id):
    conexion = connectBD()
    cursor = conexion.cursor()
    consulta_delete_bomba = sql.SQL("DELETE FROM bomba WHERE id = {}".format(id))
    cursor.execute(consulta_delete_bomba)
    conexion.commit()
    conexion.close()

def createTablePedido():
    conexion = connectBD()
    cursor = conexion.cursor()

    # Crear una tabla si no existe
    consulta_creacion_tabla_pedido = """
        CREATE TABLE IF NOT EXISTS archivo (
            id SERIAL PRIMARY KEY,
            nombre_archivo TEXT,
            contenido BYTEA
        );

        CREATE TABLE IF NOT EXISTS pedido (
            id SERIAL PRIMARY KEY,
            direccion VARCHAR(100),
            solicitante VARCHAR(40),
            telefono VARCHAR(40),
            operador VARCHAR(40),
            startpoint VARCHAR(100),
            stoppoint VARCHAR(100),
            description VARCHAR(255),
            tiempo_estimado INT,
            id_archivo INT,
            tipo VARCHAR(40),
            tiempo_real INT,
            fecha TIMESTAMP,
            FOREIGN KEY (id_archivo) REFERENCES archivo(id)
        );
    """
    cursor.execute(consulta_creacion_tabla_pedido)

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()


def insertarPedido(direccion, solicitante, telefono, operador, startpoint, stoppoint, description, tiempo_estimado, tipo):
    conexion = connectBD()
    cursor = conexion.cursor()
    
    consulta_insercion_pedido = sql.SQL("INSERT INTO pedido (direccion, solicitante, telefono, operador, startpoint, stoppoint, description, tiempo_estimado, tipo,tiempo_real,fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now())")
    datos_pedido = (direccion, solicitante, telefono, operador, startpoint, stoppoint, description, tiempo_estimado, tipo,0)
    cursor.execute(consulta_insercion_pedido, datos_pedido)


    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()


def seleccionarPedido():
    conexion = connectBD()
    cursor = conexion.cursor()

    consulta_seleccion_pedido = "SELECT * FROM pedido"

    cursor.execute(consulta_seleccion_pedido)

    resultados = cursor.fetchall()
    conexion.close()

    return resultados

def seleccionarPedido(id):
    conexion = connectBD()
    cursor = conexion.cursor()

    consulta_seleccion_pedido = "SELECT * FROM pedido WHERE id = {}".format(id)

    cursor.execute(consulta_seleccion_pedido)

    resultado = cursor.fetchall()
    conexion.close()
    
    return resultado[0]

def borrarPedido(id):
    conexion = connectBD()
    cursor = conexion.cursor()
    consulta_delete_pedido = sql.SQL("DELETE FROM pedido WHERE id = {}".format(id))
    cursor.execute(consulta_delete_pedido)
    conexion.commit()
    conexion.close()

