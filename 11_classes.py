# CLASSES: AL igual que una funcion, nos permite realizar una tarea concreta. Dotar de principio a fin un objeto.
# Debe responder a una logica concreta. Poder identificar mi codigo en un ambito de actuacion
# EScribir clases con CamelCase

# Definir una clase con constructor
class MyClass:
    def __init__(self):
        pass # Constructor de la clase, no hace nada al ser ejecutado, luego se puede trabajar

# Definir una clase
class MyEmptyPerson:
    pass # null statement, no hace nada al ser ejecutado

print(MyEmptyPerson)
print(MyEmptyPerson())

# Constructor, de alguna manera recibir parametros. Creamos una persona con nombre y apellido
class Person:
    # Constructor de clase. Obligatorio el self.
    # Alias le asignamos un valor por defecto
    def __init__(self, name, surname, alias = "Sin Alias"):
        self.name = name
        self.surname = surname
        self.alias = alias
        self.full_name = f"{name} {surname} ({alias})" # Propiedad full_name, la creamos nosotros

    # Podemos añadir más métodos a la clase (funciones). Self para invocar a la misma clase, siempre
    def walk(self):
        print(f"{self.full_name} caminando...")

my_person = Person("David","Nunez")

print(my_person.name)
print(f"{my_person.name} {my_person.surname} {my_person.alias}")
print(my_person.full_name)

my_person.walk()

my_other_person = Person("David", "Nunez", "D.N.")

print(my_other_person.full_name)

my_other_person.walk()

# Aqui cambiamos el atributo full_name
my_other_person.full_name = "Hector de Leon (El Loco de los perros)"
print(my_other_person.full_name)

# Python es de tipado dinamico
my_other_person.full_name = 666
print(my_other_person.full_name)

# Clase Person con atributos privados
class MyPerson:
    def __init__(self, name, surname, alias = "Sin Alias"):
        # Declaramos atributos privados, con dos __ antes de definir el atributo
        self.__name = name
        self.__surname = surname
        self.__alias = alias
        self.__full_name = f"{name} {surname} ({alias})"

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_alias(self):
        return self.__alias
    
    def get_full_name(self):
        return self.__full_name

    def walk(self):
        print(f"{self.get_full_name()} caminando...")

my_person = MyPerson("David","Nunez")
print(my_person.get_name())
print(my_person.get_surname())
print(my_person.get_alias())
print(my_person.get_full_name())