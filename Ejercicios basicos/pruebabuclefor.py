import datetime
import funcionsuma

print(datetime.date.today())
print(datetime.datetime.now())
"""
    este es una prueba para anexar una biblioteca de tiempo
"""
cadena = ["juan","imanol","pepito","augusto","flor"]
contador = 0

for x in cadena:
    print(x)
    if (x=="augusto"):
        print(contador)
        break
    contador += 1

funcionsuma.suma(5,6)