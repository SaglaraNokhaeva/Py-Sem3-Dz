# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

razmer=int(input("Введите размерность списка: "))
from random import randint
numbers = []
for i in range(razmer):
    numbers.append(randint(0, 10))
print(numbers)
# print(int(len(numbers)/2)+1)

numbers_multiply = []

for i in range(int(len(numbers)/2)+1):
    numbers_multiply.append()
print(numbers_multiply)