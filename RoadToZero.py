t = int(input())
for k in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if (2*a <= b):
        print((x + y)*a)
    else:
        Min = min(x, y)
        res = b * Min + a * (max(x, y) - Min)
        print(res)
