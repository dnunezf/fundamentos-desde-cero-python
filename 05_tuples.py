# Tuplas = Conjunto de valores ordenados e inmutables; una vez creada, no se puede agregar, eliminar o cambiar elementos

my_tuple = tuple() # Se define una tupla como constructor
my_other_tuple = ()

my_tuple = (21, 1.72, "David", "Nunez", "Nunez")
my_other_tuple = (21, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Nunez"))
print(my_tuple.index("David")) # Nos dice el indice en el que se encuentra el valor
print(my_tuple.index("Nunez"))

# La tupla es una coleccion ordenada e inmutable de elementos, no se puede modificar su contenido.
# my_tuple[1] = 1.80
# print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple # Si se pueden sumar
print(my_sum_tuple) 

print(my_sum_tuple[1:3]) # Entre el indice 1 y 3 (toma en cuenta el 3)

# my_tuple = [my_tuple]  # Forma de hacer que la tupla sea lista
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "UNA"
my_tuple.insert(1, "Negro")
print(my_tuple)

my_tuple = tuple(my_tuple) # forma de hacer que la lista sea tupla
print(type(my_tuple))

# del my_tuple # No funciona, lo que borra es la variable, no el contenido, no podemos hacer un del a una tupla
# del my_tuple[2] # No funciona, lo que borra es la variable, no el contenido, no podemos hacer un del a una tupla
# print(my_tuple)