# import sys
# input = sys.stdin.readline

# n=int(input())
# m=int(input())

# li = []
# for _ in range(m) :
#     li.append(list(map(int,input().split(' '))))

# f, ff = [], []
# li.sort()

# for a,b in li:
#     if a == 1 :
#         f.append(b)
#     elif (a in f) == True :
#         if ((b in ff) == False) and ((b in f) == False):
#             ff.append(b)
#     elif (b in f) == True :
#         if ((a in ff) == False) and ((a in f) == False):
#             ff.append(a)
# result = len(f) + len(ff)

# print(result)

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

invite = set()

for friend in friends[1]:
    invite.add(friend)
    for f_o_f in friends[friend]:
        invite.add(f_o_f)
print(len(invite) - 1)