s = input() + 'f'
k = 1
r = ''
# 012345
# .-.----f
while(k < len(s)):
    if (s[k] == 'f'):
        r += '0'
        break
    else:
        if (s[k] == s[k-1] and s[k] == '-'):
            k += 2
            r += '2'
        elif (s[k] == s[k-1] and s[k] == '.'):
            k += 1
            r += '0'
        elif (s[k] != s[k-1] and s[k] == '-'):
            k += 1
            r += '0'
        else:
            k += 2
            r += '1'
print(r)
