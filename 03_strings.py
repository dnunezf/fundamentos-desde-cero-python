# Strings

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"

print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"

print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"

print(my_scape_string)

my_normal_string = "\\tEste es un String \\n normalito"

print(my_normal_string)

# Formateo de Strings (%s = cadenas de string, %d = enteros). Es muy util cuando se realizan apps en varios idiomas

name, surname, age = "David", "Nunez", 21

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

# Inferencia de datos. ES la mejor forma.

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division

language_slice = language[1:3]

print(language_slice)

language_slice = language[1:]

print(language_slice)

language_slice = language[-2]

print(language_slice)

# Del caracter 0 al 6, tomalos en un rango de 2 en 2
language_slice = language[0:6:2]

print(language_slice)

# Reverse

reversed_language = language[::-1]

print(reversed_language)

# Funciones del sistema

print(language.capitalize())
print(language.upper())
print(language.count("t")) # Cuantas letras tiene
print("1".isnumeric())
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper()) # Se pueden concatenar dos funciones
print(language.startswith("py")) # Se pueden concatenar dos funciones