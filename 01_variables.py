# Variables

# Asig. CamelCase (incorrecto en Python)
MyVariable = "My String Variable"

print(MyVariable)

# Asig. SnakeCase (correcto en Python)
my_variable = "My String Variable"
my_string_variable = 'My String Variable'
my_int_variable = 5
my_bool_variable = False

print(my_variable)
print(my_string_variable)
print(my_int_variable)
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable) # Transformando en cadena de texto
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema (como type(), len())
print(len(my_int_to_str_variable))
print(len(my_string_variable))

# Variables en una sola linea. Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "David", "Nunez", "NO_ALIAS", 21
print("Me llamo:", name, surname, "mi edad es:", age, "y mi alias es:", alias)

# Inputs (name, age al inicio era David 21, pero cambio, a eso se le llama variable)
# Siempre es bueno especificar el tipo de dato en los inputs
name = input('¿Cuál es tu nombre? ')
age = int(input('¿Cuántos años tienes? '))

print(name)
print(age)

# Cambiamos el tipo de dato 
name = 35
age= "David"

print(name)
print(age)

# Forzamos el tipo (no hay problema, lo especificamos simplemente qué tipo de datos queremos)
# Python posee tipado dinamico
address: str = "Mi direccion"
address: int = 32

print(address)
print(type(address))