from collections import namedtuple
import csv
from datetime import datetime

Entreno = namedtuple("Entreno","tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido")

def lee_entrenos(ruta):
    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        registro = []
        for (tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido) in lector:
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = compartido == "S"
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M") 
            tupla = Entreno(tipo,fechahora,ubicacion,duracion,calorias,distancia,frecuencia,compartido)
            registro.append(tupla)
        return registro
    
def tipos_entreno(registro):
    tipos = []
    for linea in registro:
        tipos.append(linea.tipo)
    tipos_ord = sorted(tipos)
    tipos = set(tipos_ord)
    tipos = list(tipos)
    return tipos

def entrenos_duracion(registro,d):
    entrenos_duracion_mayor=[]
    for linea in registro:
        if linea.duracion > d:
            entrenos_duracion_mayor.append(linea)
    return entrenos_duracion_mayor

def suma_calorias(registro, f_in,f_fi):
    for linea in registro:
        