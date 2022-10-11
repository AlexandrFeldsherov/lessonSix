# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from tkinter import Y
x = input("Введите координаты первой точки : ").split(" ")
x = [int(i) for i in x]
y = input("Введите координаты второй точки : ").split(" ")
y = [int(i) for i in y]
lst = list(zip(x, y))
lst = list(map(lambda x: (x[1]**2-x[0]**2), lst))
print(sum(lst)**0.5)
