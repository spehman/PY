# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N
# целых чисел Ai (можно использовать псевдогенерацию). Последняя строка
# содержит число X.




import random
number = int(input('Введите число: '))
my_list = []
k = 0
for i in range(10):
    my_list.append(random.randint(1,101))
    min_d = max(my_list) - number

    if int(my_list[i]) == number:
        k += 1
print(f'{k} раз встречается в заданном списке число {number}')
print(f'список {my_list}')
