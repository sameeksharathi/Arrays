n = int(input())
arr = list(map(int, input().rstrip().split()))
print(' '.join(str(x) for x in arr[::-1]))
