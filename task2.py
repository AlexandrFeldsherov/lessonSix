# 2- Найти сумму чисел списка стоящих на нечетной позиции

from re import I
lst = [i for i in range(1, 5)]
sm=[i for i in lst if i % 2]
print(sum(sm))
