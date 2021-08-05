n = int(input())
listt = []

for i in range(n):
    listt.append(input())
    
list_s = set(listt)
listt = list(list_s)

listt.sort()
listt.sort(key=len)

for i in listt:
    print(i)