t = int(input())
for k in range(t):
    l, r = map(int, input().split())
    if (l <= l*2 <= r):
        print(l, l*2)
    else:
        print(-1, -1)
