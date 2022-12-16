# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math,random
from functions import give_int_num

numbers = [random.randint(0,10) for i in range(give_int_num("Введите количество элементов списка: "))]
print(f"исходный список -> {numbers}")
product_list = list(map(lambda i: (numbers[i]*numbers [-(i+1)]), [i for i in range(math.ceil(len(numbers)/2))]))
print(f"произведение пар элементов -> {product_list}")