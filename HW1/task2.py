# Задача 2: Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число:"))
n = int(n)

a1 = n % 10
n = n // 10
a2 = n % 10
n = n // 10
print("Сумма цифр числа:" , n + a1 + a2)