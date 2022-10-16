# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
mass = list(map(int, input("Введите через пробел значения массива: ").split()))
sum = 0
for i in range(0, len(mass)):
    if (i % 2 != 0):
        sum = sum + mass[i]
print(f"Сумма: {sum}")

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math
mass_ish = list(map(int, input("Введите через пробел значения массива: ").split()))
mass_res = []
for i in range(0, math.ceil(len(mass_ish) / 2)):
    mass_res.append(mass_ish[i] * mass_ish[len(mass_ish) - i - 1])
print(f"Результат: {mass_res}")

# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
import math
mass = list(map(float, input("Введите через пробел значение первого массива: ").split()))
print(mass)
max = min = math.modf(mass[0])[0]
for i in range(1, len(mass)):
    buf = math.modf(mass[i])[0]
    if buf != 0:
        if buf > max:
            max = buf
        if buf < min:
            min = buf
print(f"Результат: {format(max-min, '.2f')}")

# Напишите программу, которая будет преобразовывать десятичное число в двоичное
N = int(input('Введите целое число: '))
res = ''
while N > 0:
    res = str(N % 2) + res
    N = N // 2

# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
N = int(input('Введите целое число: '))
fib = [-1, 1]
for i in range(2, N):
    fib.insert(0, fib[1] - fib[0])
fib.extend([0, 1, 1])
for i in range(N+1, N+N):
    fib.append(fib[i] + fib[i+1])
print(fib)

