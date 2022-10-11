# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math
lst = [i for i in range (1, 21) ]
lst_2=lst[::-1]
lst=list(map(lambda x,y: x*y,lst,lst_2 ))
print(math.ceil(len(lst)/2))
lst=lst[:math.ceil(len(lst)/2)]
print(lst)