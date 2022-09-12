t = int(input())
for k in range(t):
    n = int(input())
    s = input() + '.'
    c = set()
    r = True
    for i in range(n + 1):
        if (s[i] == s[i-1]):
            continue
        else:
            if (s[i-1] in c):
                print('NO')
                r = False
                break
            else:
                c.add(s[i-1])
    if (r):
        print('YES')
