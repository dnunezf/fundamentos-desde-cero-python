# Condicionales. Representa la manera de establecer flujos de ejecucion en nuestro codigo.
# Si se cumple una condicion, se ejecuta lo que esta dentro

my_condition = True

# Es lo mismo que if my_condition == True:
if my_condition:
    print("Se ejecuta la condición del if")

print("La ejecución continúa")

# En el momento que ejecutamos una condicion del if, tiene que ser verdadera (implicito). 
# En este caso, no se ejecuta la condicion del if. 
my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")

print("La ejecución continúa")

my_condition = 5 * 5

# Le obligamos a comprobar que algo se cumpla

if my_condition == 11:
    print("Se ejecuta la condición del segundo if")

if my_condition == 10:
    print("Se ejecuta la condición del tercer if")

if my_condition >= 10:
    print("Se ejecuta la condición del cuarto if")

if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

# Debe cumplir dos condiciones (and), (or) cumple o una u otra, (not) cumple el inverso de la condicion
# else y elif necesitan condicion, else es default_case
if my_condition > 10 and my_condition < 20:
    print("Mayor que 10 y menor que 20")
elif my_condition:
    print("Igual a 25")
else:
    print("Menor o igual que 10, o mayor o igual que 20, o distinto de 25")

my_condition = 1

# En este caso, la condicion se cumple sin especificar la comprobacion (implicito).
# Es lo mismo que if my_condition == 1: 
if my_condition:
    print("Es 1")
else:
    print("Distinto de 1")

my_string = "Mi cadena de texto"

# En este caso la condicion se cumple sin especificar la comprobacion (implicito).
# Es lo mismo que if my_condition == "Mi cadena de texto"
# Si la cadena es vacia, por defecto la condicion se interpreta como False
if my_string:
    print("Mi cadena de texto no es vacia")

if my_string == "Mi cadena de texto":
    print("Estas cadenas coinciden")

my_string = ""

# Ahora si se cumple la condicion, interpreta que la cadena de texto es vacia
if not my_string:
    print("Mi cadena de texto es vacia")

# Operadores ternarios

# Ejemplo 1: Par - Impar
n = 5
res = "Even" if n % 2 == 0 else "Odd"
print(res)

# Ejemplo 2: Positivo - Negativo, utilizando nested if else

n = -5
res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(res)

# Ejemplo 3, utilizando Print Function

a = 10
b = 20

print("a is greater" if a > b else "b is greater")

# EJemplo 4, utilizando tuplas
# (condition_false, condition_true)[condition]

n = 7
res = ("Odd", "Even")[n % 2 == 0]
print(res)

# Ejemplo 5, utilizando diccionarios
# {True: value_if_true, False: value_if_false}[condition]

a = 10
b = 20
max = {True: a, False: b}[a > b]
print(max)