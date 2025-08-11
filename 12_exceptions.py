# Exception Handling: Mecanismos que, de alguna forma, evitan detener el programa cuando se produce un error.

# Python no puede sumar dos valores de distinto tipo (int + string por ejemplo)
number_one, number_two = 5, 1

number_two = "1" 

# If Else Statement NO es una solucion al manejo de errores, basicamente lo hacemos a mano

# Try Except
try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

number_two = 6

# Try Except Else
try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
# Este else statement se ejecuta si no se produce ninguna excepción, es OPCIONAL
else:
    print("La ejecucion continua correctamente")

number_two = 6

# Try Except Else Finally
try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
# Este else statement se ejecuta si no se produce ninguna excepción, es OPCIONAL
else:
    print("La ejecucion continua correctamente")
# Este finally statement se ejecuta siempre, haya o no habido una excepción, es OPCIONAL
finally:
    print("La ejecucion ha finalizado")

# Excepciones por tipo. Podemos capturar distintos tipos de excepciones, dependiente de la situacion

number_two = "2"

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")

# Captura de la informacion de la excepcion (recomendado si no se sabe la informacion de dicho error)

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
# Captura de la excepcion generica, controlar que sea lo que sea el error se controle
except Exception as error:
    print(error)