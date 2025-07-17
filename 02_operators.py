# OPERADORES ARITMETICOS

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # Resto de una division
print(10 // 3) # Division aproximada a un numero entero (redondear)
print(2 ** 3) # exponente
print(2 ** 3 + 4 - 10 / 3 * 4)

print("Hola " + "Python " + "Que tal?")

# print("Hola" + 5) --> Error, no podemos concatenar distintos tipos de datos
print("Hola " + str(5))

print("Hola" * 5) # Esto si es valido
print("Hola" * (2 ** 3)) # Esto si es valido igual

# Esto si es valido
my_float = 2.5 * 2
print("Hola" * int(my_float))

# OPERADORES COMPARATIVOS #

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print(3 > 4 == 2) # Esto es una irrealidad, pero podemos juntar operadores

# No es por cantidad de caracteres, comprueba la ordenacion alfabetica (tiene en cuenta las mayusculas y minusculas) por ASCII
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Bola") 
print("aaaa" >= "abaa") 
print("aaaa" >= "aaaa")
print("AAAA" >= "aaaa") 
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

# Si es por cantidad de caracteres
print(len("aaaa") >= len("abaa"))

# OPERADORES LOGICOS (LOGICA BOOLEANA), se pueden concatenar los operadores #

print(3 > 4 and "Hola" > "Python") # Equivale al && (AND = ^)
print(3 > 4 or "Hola" > "Python") # Equivale al || (OR = v)
print(3 < 4 and "Hola" < "Python") 
print(3 < 4 or ("Hola" < "Python" and 4 == 4)) 
print(not(3 > 4)) # Niega la condicion, equivale al !