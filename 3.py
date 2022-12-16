# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.



from functions import give_int_num
print(list(map(lambda i: ((-3)**i), [i for i in range(give_int_num("Введите число:  "))])))