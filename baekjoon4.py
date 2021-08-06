import sys
input = sys.stdin.readline

n = int(input())
listt = []

for i in range(n):
    x, y = map(int, input().split())
    listt.append([x, y])
    
listt.sort(key = lambda x : (x[0], x[1]))

for i in range(n):
    print(listt[i][0], listt[i][1])