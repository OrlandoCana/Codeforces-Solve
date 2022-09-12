t = int(input())
for k in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    Min = min(a)
    MinCandies = 0
    for boxCandies in a:
        MinCandies += (boxCandies - Min)
    print(MinCandies)
