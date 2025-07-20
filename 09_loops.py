# Loops. Mecanismo que itera, repetir algo

# While: Debemos pasarle una condicion. Se va a repetir mientras tengamos una condicion

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2 # Incrementa el valor de my_condition

my_condition = 0

# Podemos introducir un else: a manera de control de flujo del loop

while my_condition < 10:
    print(my_condition)
    my_condition += 2 # Incrementa el valor de my_condition
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

# Detener el bucle por una condicion concreta
while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print("Mi condición es 15, se detiene la ejecucion")
        break # Se detiene la ejecucion si el valor es 15

    print("Mi condición es menor que 20")

# For: Iterar un listado de elementos. Repite tantas veces como elementos iterables

my_list = [35, 24, 65, 48, 30, 17, 21]

# Imprimir y accede a cada uno de sus elementos, de su listado, iterativamente
for element in my_list:
    print(element)

# Otro ejemplo
for element in range(10):
    print(element+1)

# Otro ejemplo
for element in "Datacamp":
    if element == 'a':
        print(element)

my_tuple = (21, 1.72, "David", "Nunez", "Nunez")

for element in my_tuple:
    print(element)

my_set = {"David", "Nunez", 21} 

for element in my_set:
    print(element)

# En el caso de los diccionarios, imprime las claves por defecto
my_dict = {"Nombre":"David", "Apellido":"Nunez", "Edad": 21, 1:"Python"} # Definir el tipo de la clave y el valor

for element in my_dict:
    print(element)
else:
    print("Bucle for para diccionario ha finalizado")

# Asi se imprimen los values de las claves
for element in my_dict.values():
    print(element)
else:
    print("Bucle for para diccionario ha finalizado")

# Detener el bucle por una condicion concreta
for element in my_dict:
    print(element)
    if element == "Edad": # Se detiene si hay una clave edad
        break
else:
    print("Bucle for para diccionario ha finalizado")

# Continuar el bucle por una condicion concreta. Continue detiene la ejecucion en ese punto y vuelve al inicio del loop
for element in my_dict:
    print(element)
    if element == "Edad": # Se detiene si hay una clave edad
        continue
    print("Se ejecuta")
else:
    print("Bucle for para diccionario ha finalizado")


