t = int(input())
for k in range(t):
    n = int(input())
    Sum = 0
    even = 0
    odd = 0
    for k in map(int, input().split()):
        if (k % 2 == 0):
            even += 1
        else:
            odd += 1
        Sum += k
    if (Sum % 2 == 1):
        print('YES')
    else:
        if (even == 0):
            print('NO')
        elif (odd == 0):
            print('NO')
        else:
            print('YES')
