from collections import deque

n = int(input())

answer = deque(range(1, n+1))
  
while len(answer)>1 :
  answer.popleft()
  answer.append(answer.popleft())

print(answer[0])