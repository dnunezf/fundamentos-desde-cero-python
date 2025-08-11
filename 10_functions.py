# Functions. Intentamos encapsular una logica / problema concreto, asi evitamos duplicacion de codigo, al estar todo centralizado
# Si una tarea se centraliza en una funcion, nos resulta mas sencillo seguir el flujo de codigo.

def my_function():
    print("Esto es una función")

my_function() # Invocamos a la funcion definida
my_function() # Invocamos a la funcion definida
my_function() # Invocamos a la funcion definida

# Una funcion puede recibir, desencadenar codigo, y recibir codigo (parametros)
# Funcion que suma dos numeros

def sum_two_values(first_number, second_number):
    print(f"La suma de {first_number} y {second_number} es {first_number + second_number}")

sum_two_values(5, 7)
sum_two_values(2461, 8582)
sum_two_values("5", "7") # Tipado debil y dinamico, no forzamos el tipo de dato

# Una funcion puede recibir y retornar parametros. Hacer algo muy concreto y
# que la funcion lo retorne

def sum_two_values_with_return(first_number, second_number):
    return first_number + second_number

# Lo que retorna la funcion se debe asignar a una variable, o imprimirlo

my_result = sum_two_values_with_return(10, 5)
print(my_result)

print(sum_two_values_with_return(17, 6))

def sum_two_values_with_return_variable(first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

print(sum_two_values_with_return_variable(17, 6))

# Posibilidad de que, aunque no sigamos el orden de llamada, rectificarlo
def print_name(name, surname):
    print(f"{name} {surname}")

print_name("David", "Nunez")

# Re-ordenar
print_name(surname="Nunez", name="David")

# Parametros por defecto
def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("David", "Nunez", "Moroquito")
print_name_with_default("David", "Nunez") # Default Value

# Funcion que imprime infinitos parametros, parametros dinamicos
def print_texts(*texts):
    print(texts)

print_texts("Hola", "Python", "David")

# For loop en una funcion
def print_texts_loop(*texts):
    for text in texts:
        print(text)

print_texts_loop("Hola", "Python", "David")

# For loop en una funcion
def print_texts_upper(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_texts_upper("Hola", "Python", "David")
