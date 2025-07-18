# Listas = Es una estructura, estructurar datos. Ya nos provee operaciones de
# insercion, ordenacion, a la hora de contar tamaños. Es un conjunto de datos,
# en la que añado elementos en una posición. Forma de agrupar datos, siguiendo 
# un orden.

my_list = list() 
my_other_list = [] 

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [21, 1.72, "David", "Nunez"] # No hace falta guardar el mismo tipo de dato en una lista

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0]) # Consultamos el dato en la posicion 0
print(my_other_list[1])
print(my_other_list[-1]) # Consultamos el dato de forma inversa
print(my_other_list[-3])
print(my_other_list.count("David")) # Numero de ocurrencias de un dato      
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list) # COoncatenamos 2 listas

my_other_list.append("UNA") # INserta dato al final

print(my_other_list)

my_other_list.insert(1, "Negro") # Inserta dato en n posicion

print(my_other_list)

my_other_list[1] = "Verde" # Al igualar, modificamos el dato que habiamos insertado anteriormente, con base a su indice

print(my_other_list)

my_other_list.remove("Verde") # Elimina el dato a seleccionar

print(my_other_list)

my_list.remove(30) # Se ha eliminado el primer dato '30', distinto al del que elimina por indice

print(my_list)

print(my_list.pop()) # Pop = elimina el ultimo dato (lo conserva en memoria), devuelve el valor que desapilamos. Hacemos print unicamente para nosotros entender lo que retorna la funcion
print(my_list)

my_pop_element = my_list.pop(2) # Indice del elemento a desapilar (lo conserva en memoria)
print(my_pop_element) 
print(my_list)

del my_list[2] # Eliminamos y no conservamos en memoria el dato en n posicion
print(my_list)

my_new_list = my_list.copy() # Copiamos el contenido de la lista
print(my_new_list)

my_list.clear() # Limpia la lista completa
print(my_list)
print(my_new_list) # La copia no se ve afectada

my_new_list.reverse() # Ordena los valores al reves
print(my_new_list)

my_new_list.sort() # Por defecto, al ser Integer, ordena de menor a mayor, en caso de letras, por un orden alfabetico
print(my_new_list)

print(my_new_list[1:2]) # Entre el elemento 1 y 2, esta el 30
print(my_new_list[1:3]) # Entre el elemento 1 y 3, esta el 30, 35

# Tipado dinamico, cambiamos el tipo de dato 
my_list = "Hola Python"
print(my_list)
print(type(my_list))