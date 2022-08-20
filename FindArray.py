t = int(input())
for k in range(t):
    n = int(input())
    print(" ".join([str(k) for k in range(3, 2*n + 3, 2)]))
