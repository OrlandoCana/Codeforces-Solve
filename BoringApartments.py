t = int(input())
for k in range(t):
    x = input()
    s = len(x)
    l = int(x[0])
    print(s*(s+1)//2 + 10*(l-1))
