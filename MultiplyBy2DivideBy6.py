t = int(input())
for k in range(t):
    n = int(input())
    cont = 0
    while(not n % 6):
        cont += 1
        n //= 6
    while(not n % 3):
        cont += 2
        n //= 3

    if (n == 1):
        print(cont)
    else:
        print(-1)
