# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.

n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))

def sum(a,b):
    if b == 0:
        return a
    else:
        return sum(a, b-1) + 1

print (sum(n, m))
