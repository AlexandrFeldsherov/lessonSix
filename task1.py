# 1- Определить, присутствует ли в заданном списке строк, некоторое число

from ast import Try


lst = [i for i in range (1, 21) ]
print (lst)
x=int(input("Введите число : "))
y=[i for i in lst if i==x]
try:
    y[0]==x
    print("Число в списке есть")
except:
    print("Числа в списке нет")

