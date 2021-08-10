n = int(input())
stack = []
answer = []
nownum = 1
check = False

for i in range(n):
    m = int(input())
    
    while nownum <= m:
        stack.append(nownum)
        answer.append("+")
        nownum+=1
        
    if stack[-1]==m:
        stack.pop()
        answer.append("-")
    else:
        check = True
            
if check==False:
    for i in answer:
      print(i)
else:
    print("NO")