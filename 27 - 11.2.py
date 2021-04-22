fi = open("27-10b.txt")
n = int(fi.readline())
sm = 0
raz = []
raz_1 = []

for i in range(n):
    a = list(map(int, fi.readline().split()))
    a.sort()
    sm += a[2]
    if (a[2] - a[1]) % 8 == 0:
        raz.append([a[2] - a[1],(a[2] - a[1]) % 8, i])
    if (a[2] - a[0]) % 8 == 0:
        raz_1.append([a[2] - a[0],(a[2] - a[0]) % 8, i])


print(sm, sm % 8)
raz.sort()
raz_1.sort()
print(raz)
print(raz_1)