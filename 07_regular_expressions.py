# Regular Expressions

import re # re es regular expression

# Match

my_string = "Esta es la lección número 7"
my_other_string = "Esta no es la lección número 6"

print(re.match("Esta es la lección", my_string)) # Quiero saber si mi texto tiene esto
print(re.match("es la lección", my_string)) # No aparece porque busca desde el principio

print(re.match("Esta es la lección", my_string, re.I)) # con el re.I ignora, hay varios

match = re.match("Esta es la lección", my_string, re.I)
print(match)
print(match.span()) # Marca valores en los que empieza y termina
start, end = match.span()
print(my_string[start:end]) #Muestra el texto entre esos valores

match = re.match("Esta no es la lección", my_other_string)
if match is not None:
    print(match)
    start, end = match.span()
    print(match.span())
    print(my_other_string[start:end])

# Search

search = re.search("lección", my_string, re.I) # A diferencia de Match, Search no necesita desde el principio
print(search) # Solo encuentra la palabra una vez
start, end = search.span()
print(search.span())
print(my_string[start:end])

# Findall

findall = re.findall("lección", my_string, re.I) # A diferencia de Search, Findall encuentra la palabra todas las veces que esta
print(findall)

# Split

print(re.split("i", my_string)) # Separa la frase en sa letra

# Sub

print(re.sub("[L/l]ección", "LECCIÓN", my_string, re.I)) # Cambia formato

# Patterns      Distintas maneras de buscar

pattern = r'[lL]ección'
print(re.findall(pattern, my_string))

pattern = r'[lL]ección|número'
print(re.findall(pattern, my_string))

pattern = r'[a-z]'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))

pattern = r'\d'   # También busca caracteres numericos
print(re.findall(pattern, my_string))

pattern = r'\D'   # Tambien busca caracteres no numericos
print(re.findall(pattern, my_string))

pattern = r'[l].*'  # Buscaen la oracion a partir de la l
print(re.findall(pattern, my_string))

# Email validation

email = "grimati@grimati.com"
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))
