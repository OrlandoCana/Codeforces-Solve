t = int(input())
for i in range(t):
    x, y, n = map(int, input().split())
    r = n % x
    if (r > y):
        k = n - (r - y)
    elif(r < y):
        k = n - r - (x - y)
    else:
        k = n
    print(k)
