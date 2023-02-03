# 1. Дано целое число k > 2.
# Напечатать все числа из диапазона 2, k,
# не являющиеся простыми.
from check_num import check_num

n = input("Введите конец диапазона: ")
while check_num(n) == False or int(n)<=2:
    n = input("Повторите ввод: ")

n = int(n)
any_num = False
for i in range(2,n+1):
    k = 0
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            k = k + 1
    if (k > 0):
        print(i)
        any_num = True

if any_num == False:
    print("Числа не являющиеся простыми не найдены!")

