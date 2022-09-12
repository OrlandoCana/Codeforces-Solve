t = int(input())
for k in range(t):
    n, k = map(int, input().split())
    a = list(sorted(map(int, input().split())))
    b = list(sorted(map(int, input().split())))[::-1]
    suma = 0
    for j in range(k):
        if (a[j] < b[j]):
            suma += b[j]
        else:
            suma += a[j]
    for j in range(k, n):
        suma += a[j]
    print(suma)
