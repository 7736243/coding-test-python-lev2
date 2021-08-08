import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
deq = deque()

for i in range(n):
  a = input().split()
  
  if a[0]=="push_front":     deq.appendleft(int(a[1]))
  elif a[0]=="push_back":    deq.append(int(a[1]))
  elif a[0]=="pop_front":
    if len(deq)==0:    print("-1")
    else:    print(deq.popleft())
  elif a[0]=="pop_back":
    if len(deq)==0:    print("-1")
    else:    print(deq.pop())
  elif a[0]=="size":    print(len(deq))
  elif a[0]=="empty":
    if len(deq)==0: print("1")
    else: print("0")
  elif a[0]=="front":
    if len(deq)==0: print("-1")
    else: print(deq[0])
  elif a[0]=="back":
    if len(deq)==0: print("-1")
    else: print(deq[-1])