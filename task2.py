# 2. Написать программу, в которую пользователь вводит
# две строки неограниченной длины,
# содержащие версии программ.
#
# Версия программы – это строка их 4-х чисел, разделенных точками.
# Числа целые положительные или ноль. Могут начинаться с нулей.
# Обработка должна определить, какая из версий старше.

import re

def check_ver(version):
    if re.fullmatch(r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*', version):
        print(version, ": версия корректна!")
        return True
    else:
        print("Версия некорректна!")
        return False

ver1 = input("Введите первую версию \n")
while check_ver(ver1) == False :
    ver1 = input("Повторите ввод: ")
ver2 = input("Введите вторую версию \n")
while check_ver(ver2) == False :
    ver2 = input("Повторите ввод: ")

if ver1 == ver2:
    print("Версии одинаковые")
    exit()

splitted_ver1 = ver1.split('.')
splitted_ver2 = ver2.split('.')
#check = 0
for i in range(0,4):
    if splitted_ver1[i] > splitted_ver2[i]:
        print(ver1," старше чем ", ver2)
        #check = 1
        exit()
    elif splitted_ver1[i] < splitted_ver2[i]:
        print(ver2, " старше чем ", ver1)
        #check = -1
        exit()
