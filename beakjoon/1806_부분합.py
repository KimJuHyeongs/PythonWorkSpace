# 합이 s 이상 중, 가장 짧은 것
# import sys
# input = sys.stdin.readline

# if __name__ == "__main__":
#     n,s = map(int,input().split())
#     li = list(map(int,input().split()))
#     result = n+1
#     for start in range(n-1):
#         end, val = start,li[start]    
#         while val < s and end < n-1:
#             end += 1
#             val += li[end]
#         if val >= s:
#             result = min(result, end - start + 1)
    
#     if result > n:
#         print(0)
#     else :
#         print(result)

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n,s = map(int,input().split())
    li = list(map(int,input().split()))
    for i in li:
        if i >= s:
            print(1)
            exit(0)
    val, end, result= li[0], 0, n+1
    for start in range(n-1):
        flag = True
        while end < n and flag:
            if val >= s:
                for idx in range(end, start, -1):
                    if val - li[idx] >= s:
                        val= val - li[idx]
                    else :
                        result = min(result, end - start + 1)
                        end, flag, val = idx, False, val - li[start]
                        break
            else:
                if end == n-1 : break
                end += 1
                val += li[end]
    if result >= n+1:
        print(0)
    else :
        print(result)