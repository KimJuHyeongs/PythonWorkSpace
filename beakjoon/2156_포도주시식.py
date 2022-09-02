import sys
input = sys.stdin.readline

wine = []
for _ in range(int(input())) :
    wine.append(int(input()))
dp = [0]*len(wine)

if len(wine) == 1 :
    print(wine[0])
elif len(wine) == 2 :
    print(max(wine[0], wine[0] + wine[1]))
else :
    dp[0] = wine[0]
    dp[1] = max(wine[0], wine[0] + wine[1])
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2])
    for i in range(3,len(dp)) :
        dp[i] = max( (max(dp[:i-2])+wine[i-1]+wine[i]) , (max(dp[:i-1])+ wine[i]) )
    print(max(dp))


##모범답안
# import sys
# I=sys.stdin.readline
# a=[int(I())for i in range(int(I()))]
# d=[0,a[0],0]
# for i in a[1:]:
#     d=[max(d),d[0]+i,d[1]+i]  
# print(max(d))