# блок переменных

fi = open("27-10b.txt")
n = int(fi.readline())
sm = 0
raz = []
raz_1 = []

for i in range(n):
    a = list(map(int, f.readline().split())) # запись ввиде массива
    a.sort() # сортировка
    sm += a[2] # сумма максимальных
    if (a[2] - a[1]) % 4 != 0: # разность 3 и 2 элеменнтов
        raz.append(a[2] - a[1])
    if (a[2] - a[1]) % 4 != 0: # разность 3 и 1 элементов
        raz_1.append(a[2] - a[0])
 
print(sm, sm % 4)
raz.sort()
raz_1.sort()
print(raz)
print(raz_1)