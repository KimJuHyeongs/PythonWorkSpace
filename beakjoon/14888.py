# # import sys
# # from itertools import permutations
# # input = sys.stdin.readline

# # if __name__ == '__main__' :
# #     n = int(input())

# #     val = list(map(int,input().split(' ')))
# #     num_oper = list(map(int,input().split(' ')))

# #     oper, cal, result = ['+', '-', '*', '/'], [], []
    
# #     for idx in range(len(num_oper)) :
# #         for _ in range(num_oper[idx]) :
# #             cal.append(oper[idx])
    
# #     per = list(set(permutations(cal,len(cal))))

# #     for p in per :
# #         v = val[0]
# #         for idx in range(len(p)) :
# #             if p[idx] == '+' :
# #                 v += val[idx + 1]
# #             elif p[idx] == '-' :
# #                 v -= val[idx + 1]
# #             elif p[idx] == '*' :
# #                 v *= val[idx + 1]
# #             else :
# #                 if v < 0 :
# #                     v = -((-v) // val[idx + 1])
# #                 else :
# #                     v //= val[idx + 1]

# #         result.append(v)
    
# #     print(max(result))
# #     print(min(result))

import sys
input = sys.stdin.readline

def backtracking(prevVal, size, idx, plus, minus, multi, divide) :
    global max_val, min_val
    
    if size == n-1 :
        if max_val < prevVal :
            max_val = prevVal
        if min_val > prevVal :
            min_val = prevVal
    
    else :
        if plus :
            backtracking(prevVal + val[idx], size+1, idx+1, plus-1, minus, multi, divide)
        if minus :
            backtracking(prevVal - val[idx], size+1, idx+1, plus, minus-1, multi, divide)
        if multi :
            backtracking(prevVal * val[idx], size+1, idx+1, plus, minus, multi-1, divide)
        if divide :
            if prevVal < 0 :
                backtracking(-((-prevVal) // val[idx]), size+1, idx+1, plus, minus, multi, divide-1)
            else :
                backtracking(prevVal // val[idx], size+1, idx+1, plus, minus, multi, divide-1)

if __name__ == '__main__' :
    n = int(input())

    val = list(map(int,input().split()))
    num_oper = list(map(int,input().split()))

    max_val, min_val = -(10**9+1), 10**9+1
    backtracking(val[0], 0, 1, *num_oper)

    print(max_val, min_val, sep='\n')