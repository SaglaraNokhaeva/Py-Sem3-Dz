# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = []
# for x in y:
#     a.append(x)
#     a = np.array(a)

dec_number=int(input("Введите число в десятичной системе счисления: "))
bin_number=[]
i=0
while dec_number>1:
    bin_number.append(dec_number%2)
    print(bin_number[i])
    k=int(dec_number%2)
    dec_number=k
    print(dec_number)
    i+=1
print(bin_number)