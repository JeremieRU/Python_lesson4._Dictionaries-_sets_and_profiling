# 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

a = int(input("Введите количество эхлементов списка А: "))
b = int(input("Введите количество эхлементов списка B: "))

mina = int(input("Введите минимальное значение списка A: "))
maxa = int(input("Введите максимальное значение списка A: "))
minb = int(input("Введите минимальное значение списка B: "))
maxb = int(input("Введите максимальное значение списка B: "))

lista = []
listb = []

for i in range (a):
    lista.append(random.randint(mina, maxa))
for i in range (b):
    listb.append(random.randint(minb, maxb))

print(lista)
print(listb)

listtmp = []

for i in lista:
    if i in listb:
        listtmp.append(i)

print(listtmp)

listtmp = set(listtmp)

print(listtmp)

print(sorted(listtmp))