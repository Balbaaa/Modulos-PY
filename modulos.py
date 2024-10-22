# Resolver cada uno de los pasos debajo de cada consigna.

print("---Actividad 01 - random---")
print() # El print() vacío se usa para generar un espacio en la consola.

# 1.- Importar el módulo random.
import random as rd


# 2.- Crear 5 variables, donde cada una guarde un número aleatorio (no se puede repetir el rango seleccionado).
numerouno = rd.randrange(10)
numerodos = rd.randrange(34)
numerotres = rd.randrange(120)
numerocuatro = rd.randrange(45)
numerocinco = rd.randrange(20)

# 3.- Hacer un print() de cada número.
print(numerouno)
print(numerodos)
print(numerotres)
print(numerocuatro)
print(numerocinco)
# 4.- Sumar los números generados y guardar el resultado en una variable.
suma = str(numerouno + numerodos + numerotres + numerocuatro + numerocinco)

# 5.- Hacer un print() con el texto "La suma de los números generados es: " y concatenar el resultado de la suma.
print("La suma de los generados es:" + " " + suma)

# Fin de la actividad 01----------------------

print()
print("---Actividad 02 - datetime---")
print()

# 1.- Importar el módulo datetime.

import datetime as dt

# 2.- Crear una variable llamada “ahora” y, dentro de ella, guardar la fecha actual con esta función → datetime.datetime.now(). 
# Luego, realizar un print().
ahora = dt.datetime.now()
print(ahora)

# 3.- Crear una variable llamada “fecha” y, dentro de ella, guardar la fecha de tu cumpleaños con esta función → datetime.datetime(AÑO, MES, DÍA).
# Luego, realizar un print().
fecha = dt.datetime(2006, 7, 26)
print(fecha)

# 4.- Crear una variable llamada “diferencia”, que guarde el resultado de restar las variables “ahora” y “fecha”. Luego, realizar un print().

diferencia = ahora - fecha
print(diferencia)

# 5.- Crear una variable llamada “diferenciaEnDias” y dentro de ella escribir → diferencia.days, para guardar solo los días de la resta anterior. 
# Luego, realizar un print().

diferenciaEnDias = diferencia.days
print(diferenciaEnDias)

# 6.- Crear una variable llamada “anios”, que guarde el resultado de dividir a la variable “diferenciaEnDias” en 365, 
# para que nos devuelva el número en años. Luego, realizar un print().

anios = diferenciaEnDias / 365
print(anios)

# 7.- Realizar un print() con el texto → "Tengo ____ años" (Lo puedes hacer concatenando).

print("Tengo" + " " + str(int(anios)) + " " + "años")

# TIP: Para eliminar los decimales de un número, puedes pasarlo a entero con la función "int()" 
# y después pasarlo a string "str()" para poder concatenarlo en el print().


# Fin de la actividad 02------------------------------------