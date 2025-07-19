# Dictionaries. Un diccionario utiliza un hash map internamente. Almacena elementos como pares de
# clave-valor. En los diccionarios se accede a los valores utilizando una clave unica.
# Se agrupa por pares de valores (relacion clave-valor). Estructura para relacionar datos.

my_dict = dict() # Se define un diccionario como constructor
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"David", "Apellido":"Nunez", "Edad": 21, 1:"Python"} # Definir el tipo de la clave y el valor


my_dict = {
    "Nombre":"David", 
    "Apellido":"Nunez", 
    "Edad": 21, 
    "Lenguajes": {"Python", "Java", "C"}, # Como clave tiene un string, pero como valor tiene un set dentro
    1:1.72
}

print(my_other_dict)
print(my_dict) 

print(len(my_other_dict))
print(len(my_dict)) # No confundir que dentro de un diccionario haya una estructura compleja, como un set. Son 5 valores, no 8

print(my_dict["Nombre"]) # Muestra el valor de la clave

# Cambiamos el valor de la clave
my_dict["Nombre"] = "Juan"
print(my_dict["Nombre"])
print(my_dict[1])

# Agregamos una nueva clave-valor al diccionarios
my_dict["Institucion"] = "UNA"
print(my_dict)

# Eliminar un elemento de nuestro diccionario, a traves de la clave
del my_dict["Institucion"]
print(my_dict)

print("David" in my_dict) # False, ya que filtra por clave, no valor
print("Apellido" in my_dict) # True

print(my_dict.items()) # tenemos un listado con cada uno de los items
print(my_dict.keys()) # solo retorna un listado de las claves
print(my_dict.values()) # solo retorna un listado de los valores
# print(my_dict.fromkeys(("Nombre", 1))) # None

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # De esta forma, creamos un diccionario SIN VALORES, pero no conserva los valores.
print(my_new_dict)

# Creamos una lista y se la pasamos al diccionario. No provoca error
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))

# Esta es la verdadera utilidad del fromkeys. Creamos un nuevo diccionario que aprovecha las claves del diccionario a copiar, y luego lo rellenamos
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

# Le insertamos a todos los elementos "David", "Nunez". No podemos insertar un valor a una clave especifica.
my_new_dict = dict.fromkeys(my_dict, ("David", "Nunez"))
print((my_new_dict))