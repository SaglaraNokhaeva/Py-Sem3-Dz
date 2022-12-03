# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
dec_number=int(input("Введите число в десятичной системе счисления: "))
bin_number=[]
i=0
while dec_number>1:
    bin_number.append(dec_number%2)
    dec_number=int(dec_number/2)
bin_number.append(dec_number%2)
bin_number.reverse()
print(*bin_number, sep="")