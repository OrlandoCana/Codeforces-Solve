t = int(input())
for k in range(t):
    a, b = map(int, input().split())
    if (a == b):
        print(4*(a**2))
    else:
        mi = min(a, b)
        ma = max(a, b)
        if (mi*2 >= ma):
            print((mi*2)**2)
        else:
            print(ma**2)
