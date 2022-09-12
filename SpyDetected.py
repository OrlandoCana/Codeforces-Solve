t = int(input())
for k in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    j = 2
    while (j < n):
        if (l[j] == l[j - 1]):
            if (l[j] == l[j - 2]):
                j += 1
            else:
                print(j - 1)
                break
        else:
            if (l[j] == l[j - 2]):
                print(j)
            else:
                print(j + 1)
            break
