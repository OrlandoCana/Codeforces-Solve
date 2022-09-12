n, k = map(int, input().split())
l = list(map(int, input().split()))

numParticipants = 0
for num in l:
    if (num > k):
        numParticipants += 1
print(numParticipants)
