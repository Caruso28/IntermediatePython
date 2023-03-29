# Challenge

"""
FIZZ BUZZ
Escribe un programa que muestre por consola (con un print) los numeros del 1 al 100 
(ambos incluidos y con un salto de linea entre cada funcion) sustituyendo los siguientes:
- Multiplos de 3 con la palabra "Fizz"
- Multiplos de 5 con la palabra "Buzz"
- Multiplos de 3 y de 5 con la palabra "FizzBuzz"
"""
def fizzbuzz():
    for index in range(1, 101):    
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 5 == 0:
            print("Buzz")
        else:
            print(index)
fizzbuzz()

"""
Escriba una funcion que reciba 2 palabras (strings) y retorne un verdadero o falso (bool)
según sean o no anagramas.
- Un anagrama cnsiste en formar una palabra reordenando TODAS las letras de otra palabra inicial
- No hace falta comprobar que ambas palabra existan
- Dos palabras exactamente iguales no son anagramas
"""
def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())
print(is_anagram("amor", "roma"))

"""
Escriba un programa que imprima los primeros 50 terminos de la sucesion de Fibonaccci, empezando en 0.
"""
def fibonacci():
    prev = 0
    next = 1
    for index in range(0, 50):
            print(prev)
            fib = prev + next
            prev = next
            next = fib
(fibonacci())

"""
Escribe un rograma que se encargue de comprobar si un numero es o no primo.
Hecho esto imprime los numeros primos entre 1 y 100
"""
def is_prime():

    for number in range(1, 101):
        if number >= 2:
            
            is_divisible = False

            for index in range(2, number):    
                if number % index == 0:
                    is_divisible = True
            if not is_divisible:
                print(number)
is_prime()

"""
Crer un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que
lo haga de forma automatica
"""
def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text == text[text_len - index - 1]
    return reversed_text
print(reverse("Hola Mundo"))
