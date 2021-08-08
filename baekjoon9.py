from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

cnt = Counter(arr)

for i in arr2:
  print(cnt[i], end = " ")