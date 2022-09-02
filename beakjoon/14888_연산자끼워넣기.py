import sys
from itertools import permutations
input = sys.stdin.readline

cal,result = [],[]
N = int(input())
number = list(map(int,input().split(' ')))
num_cal = list(map(int,input().split(' ')))
oper = ['+','-','*','/']
for i in range(len(num_cal)):
    for _ in range(num_cal[i]):
        cal.append(oper[i])

per = list(set(permutations(cal,len(cal))))

for i in per:
    tmp = number[0]
    for j in range(len(i)):
        if i[j] == '+':
            tmp += number[j+1]
        elif i[j] == '-':
            tmp -= number[j+1]
        elif i[j] == '*':
            tmp *= number[j+1]
        else :
            if tmp < 0 :
                tmp = -((-tmp) // number[j+1])
            else :
                tmp //= number[j+1]
    result.append(tmp)

print(max(result))
print(min(result))


# # 모범답안
# import sys
# input = sys.stdin.readline

# N = int( input() )
# nums = list( map( int, input().split() ) )
# oper = list( map( int, input().split() ) )

# def backtrack( prevVal, size, idx, plus, minus, multi, divide ):
# 	global max, min
# 	if size == N - 1:
# 		if max < prevVal:
# 			max = prevVal
# 		if min > prevVal:
# 			min = prevVal
# 	else:
# 		if plus:
# 			backtrack( prevVal + nums[idx], size + 1, idx + 1, plus - 1, minus, multi, divide )

# 		if minus:
# 			backtrack( prevVal - nums[idx], size + 1, idx + 1, plus, minus - 1, multi, divide )

# 		if multi:
# 			backtrack( prevVal * nums[idx], size + 1, idx + 1, plus, minus, multi - 1, divide )

# 		if divide:
# 			if prevVal < 0:
# 				backtrack( -(abs(prevVal) // nums[idx]), size + 1, idx + 1, plus, minus, multi, divide - 1 )
# 			else:
# 				backtrack( prevVal // nums[idx], size + 1, idx + 1, plus, minus, multi, divide - 1 )
# max = -(10**9+1)
# min = 10 ** 9 + 1
# backtrack( nums[0], 0, 1, *oper )
# print( max, min, sep = '\n' )
