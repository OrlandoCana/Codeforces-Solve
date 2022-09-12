a = []
i = 1
l = 0
while(l < 1000):
    if (i % 3 != 0 and i % 10 != 3):
        a.append(i)
        l += 1
    i += 1

t = int(input())
for i in range(t):
    k = int(input())
    print(a[k - 1])
