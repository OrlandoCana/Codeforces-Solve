t = int(input())
for k in range(t):
    n = int(input())
    if ((n//2) % 2 == 0):
        print('YES')
        aux = n//2 - 1
        r, x = '', ''
        j, i = 1, 2
        suma = 0
        while (aux):
            x += str(j) + ' '
            r += str(i) + ' '
            suma += 1
            aux -= 1
            j += 2
            i += 2
        print(r + str(n) + ' ' + x + str(suma + n))
    else:
        print('NO')
