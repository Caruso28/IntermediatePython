# Error Types

# SyntaxError
#print "Hola Comunidad" #Descomentar para error
print("Hola Comunidad")

# NameError
language = "Spanish" #Comentar para error
print(language)

# IndexError
my_list = ["Pyhton", "Swift", "Katlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) # No existe

# ModuleNotFoundError
#import maths #Descomentar para error
import math

# AtributeError
#print(math.PI) #Descomentar para error
print(math.pi)

# KeyError
my_dict = {"Nombre":"Guido", "Apellido":"Rimati", "Edad":37} 
print(my_dict["Edad"])
#print(my_dict["Apelido"]) #Descomentar para error
print(my_dict["Apellido"])

# TypeError
#print(my_list["0"]) #Descomentar para error
print(my_list[0])

# importError
# from math import PI #Descomentar para error
from math import pi
print(pi)

# ValueError
my_int = "10"
print(type(my_int))

my_int = int("10")
print(type(my_int))

#my_int = int("10 años") # Descomentar para error
print(type(my_int))

# ZeroDivisionError
print(4/2)
# print(4/0) # Descomentar para error