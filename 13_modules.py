# Modulos: Codigo externo a nuestro fichero o código, que podemos reutilizar.
# Codigo que, si yo tengo acceso a él, puedo utilizarlo en mi programa.
# Evita duplicidad

import module # ---> de aqui importamos TODO de module.py
# from 10_functions import sum_two_values ---> nomenclatura incorrecta, no se puede llamar un modulo con un numero al inicio

# Accedemos a la funcion que trabajamos en module.py (solo funciona si se importa todo de module)
module.sumValues(1, 2, 3)
module.printValue("Hola, Python")

# Aqui especificamos lo que queremos realmente importar
from module import sumValues, printValue 

sumValues(1, 2, 3)
printValue("Hola, Python")

# Modulos propios del sistema Python
import math # Modulo matematico de Python
import random # Modulo aleatorio de Python

print(math.pi)
print(random.randint(1, 10)) # Genera un numero aleatorio entre 1 y 10
print(math.pow(2, 8)) 

from math import pi as PI_VALUE # Importamos pi de math y le asignamos un nuevo nombre

print(PI_VALUE)
