# Set = De base tiene un array. Es un conjunto, coleccion no ordenada de elementos únicos.
# No permite elementos duplicados y no tiene un orden definido, por lo que no se pueden acceder
# a sus valores por indice.

my_set = set() # Se define un set como constructor
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"David", "Nunez", 21} # Ahora es un set
print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set[1]) # Error, no podemos acceder a indices en un set

my_other_set.add("dnunezf")
print(my_other_set) # Set no es estructura ordenada, utiliza un hash para meter todos los elementos

my_other_set.add("dnunezf")
print(my_other_set) # Set no permite elementos duplicados, solo se añade un dnunezf

# Comprobar que un elemento existe en un set
print("David" in my_other_set)
print("Davidcito" in my_other_set)

my_other_set.remove("dnunezf") # Elimina un valor dentro del set
print(my_other_set)

my_other_set.clear() # Limpia el contenido del set 
print(my_other_set)
print(len(my_other_set))

#del my_other_set # Error, no se puede, hemos eliminado nuestra variable
#print(my_other_set)

# Convertimos nuestro set a una lista
my_set = {"David", "Nunez", 21} 
my_list = list(my_set)
print(my_list)
print(my_list[0])

# Unimos dos set
my_other_set = {"C", "C++", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set)) # No pasa nada, no se duplica, no acepta repetidos
print(my_new_set.union(my_new_set).union({"JavaScript", "C#"})) # Aqui, aplicamos un union a elementos que no existen anteriormente, si funciona

print(my_new_set.difference(my_set)) # De my_new_set, le quitamos los elementos de my_set