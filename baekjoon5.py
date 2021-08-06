n = int(input())
listt = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    listt.append((age, name))
    
listt.sort(key = lambda x : (x[0]))

for i in listt:
    print(i[0], i[1])