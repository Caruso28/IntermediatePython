# Higher Order Functions

from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value (first_value, second_value, f_sum):
    return f_sum(first_value+ second_value)

print(sum_two_values_and_add_value(2, 5, sum_one))
print(sum_two_values_and_add_value(2, 5, sum_five))

# Clausures

def sum_ten():
    def add(value):
        return value + 10
    return add

add_clausure = sum_ten()
print(add_clausure(5))

#Puedo darle valores

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_clausure = sum_ten(1)
print(add_clausure(5))
# Y tambien Lambda
sum_ten(5)(1)

# Bulit-in Higher Order Function

numbers = (2, 5, 10, 21, 3, 30)

# Map  Itera la lista

def multiply_two(number):
    return number * 2
print(list(map(multiply_two, numbers)))
# Tambien con Lambdas
print(list(map(lambda number: number * 2, numbers)))

# Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
# Tambien con lambdas
print(list(filter(lambda number: number > 10, numbers)))

# Reduce 
# se tiene que importar

def sum_two_values(first_value, second_value):
    return first_value + second_value
print(reduce(sum_two_values, numbers))
# El resultado no es una lista sino en este caso una sumatoria, primer valor el acumulado hasta ahi