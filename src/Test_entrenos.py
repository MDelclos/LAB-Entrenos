from Entrenos import *
def test_lee_entreno():
    print("Probando lee_entrenos...")
    datos = lee_entrenos("data/entrenos.csv")
    for i in datos[:10]:
        print(i)
def test_tipo_entreno():
    tipos_entreno(lee_entrenos("data/entrenos.csv"))
def test_entrenos_duracion():
    lista_duracion = entrenos_duracion(lee_entrenos("data/entrenos.csv"),120)
    for i in lista_duracion:
        print(i)
if __name__=="__main__":
    Entreno = namedtuple("Entreno","tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido")
    # test_lee_entreno()
    # test_tipo_entreno()
    test_entrenos_duracion()
    
    