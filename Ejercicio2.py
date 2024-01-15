import csv


def convertir_mayuscula(texto):
    return texto.upper()

def leer_archivo(archivo):
    with open(archivo) as File:
        lectura = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for i in lectura:
            i[0] = convertir_mayuscula(i[0])
            
            print(i[0])


leer_archivo('50.csv')