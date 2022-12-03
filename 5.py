# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных 
# индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k=int(input("Введите число: "))
Fibbonachi_list=[]
Fibbonachi_list.append(0)
Fibbonachi_list.append(1)
if k>1:
    i=2
    while i<(k+1):
        Fibbonachi_list.append(Fibbonachi_list[i-2]+Fibbonachi_list[i-1])
        i+=1
Fibbonachi_list.reverse()
Fibbonachi_list.append(1)
if k>1:
    i=k+2
    while i<(2*k+1):
        Fibbonachi_list.append(Fibbonachi_list[i-2]-Fibbonachi_list[i-1])
        i+=1
Fibbonachi_list.reverse()
print(Fibbonachi_list)