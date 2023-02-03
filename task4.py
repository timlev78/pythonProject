# 4. Заполнить двумерный массив,
# как показано на рисунке: https://disk.yandex.ru/i/uYoks27FjK8z3Q

mas = [[0,0,0,0,0,0,0,0,0,0] for i in range(12)]
elem = 120
j = 10
for i in range(0,12):

    if j+1 > 9:
        j-=1
        while j-1 >= -1:
            mas[i][j] = elem
            elem-=1
            j-=1
    elif j-1 < 0:
        j+=1
        while j+1 <= 10:
            mas[i][j] = elem
            elem-=1
            j+=1

for i in range(0,12):
    print(mas[i])