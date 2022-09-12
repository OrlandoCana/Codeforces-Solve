t = int(input())
for k in range(t):
    n = int(input())
    j = -1
    even = 0
    odd = 0
    for num in map(int, input().split()):
        j += 1
        if (num % 2 == j % 2):
            continue
        else:
            even += [0, 1][num % 2 == 0]
            odd += [0, 1][num % 2 == 1]

    print(f"{[-1, even][even == odd]}")
