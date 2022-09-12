t = int(input())
for k in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(max(l) - min(l))
