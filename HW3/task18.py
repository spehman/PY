# Задача 18:
# Требуется найти в массиве A самый близкий по величине элемент к 
# заданному числу X. Если таких элементов несколько, вы вывести один любой.
# Пользователь в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны N целых чисел Ai
# (можно использовать псевдогенерацию). Последняя строка содержит число X


import random
number = int(input('Введите число: '))
my_list = []
k = 0
closest_num = -1
for i in range(10):
    my_list.append(random.randint(1,101))
    min_d = max(my_list) - number
    if int(my_list[i]) == number:
        k += 1
for i in set(my_list):
    if abs(i - number) < min_d:
        min_d = abs(i - number)
        closest_num = i
print(f'максимально близкое число {closest_num}')
print(f'список {my_list}')
