import os, sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from collections import deque, defaultdict

s = input()
d = defaultdict(lambda : 0)
for i in s:
    d[i] += 1

ctr = 0
od = []
ev = []
for i in d:
    if d[i]%2:
        ctr += 1
        od.append([i, d[i]])
    else:
        ev.append([i, d[i]])
# print(d)
if ctr >= 2 or (ctr == 1 and len(s)%2 == 0):
    print("NO SOLUTION")
else:
    left = []
    right = []
    while ev:
        left.append(ev[-1][0])
        right.append(ev[-1][0])
        ev[-1][1] -= 2
        if ev[-1][1] == 0:
            ev.pop()
    while od:
        left.append(od[-1][0])
        od[-1][1] -= 1
        if od[-1][1] == 0:
            break
        right.append(od[-1][0])
        od[-1][1] -= 1
        if od[-1][1] == 0:
            break
    print("".join(left + right[::-1]))

