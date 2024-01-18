import csv
import cProfile

def convertir_mayuscula(texto):
    return texto.upper()

def letra_dni(numero):
    letra_dni = {0:'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X',
                     11: 'B', 12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C',
                     21: 'K', 22: 'E'}
    
    resto = int(numero)%23
    if resto in letra_dni:
        return letra_dni[resto]
    
def leer_archivo(archivo):
    with open(archivo) as csvfile:
        lectura = csv.reader(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for i in lectura:
            i[0] = convertir_mayuscula(i[0])
            print('{} con DNI: {}{}'.format(i[0], i[1], letra_dni(i[1])))
            

cProfile.run("leer_archivo('50.csv')")