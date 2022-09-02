def solution(n):
    cnt, num = 9, 10
    
    while True:
        s_num = str(num)
        flag = True
        for idx in range(1,len(s_num)):
            if s_num[idx] < s_num[idx-1]:
                continue
            else :
                start = s_num[:idx-1]
                mid = str(int(s_num[idx-1])+1)
                end = '0' + s_num[idx+1:]
                num, flag = int(start + mid + end), False
                break
        
        if flag:
            cnt += 1
            if cnt == n:
                return num
            num += 1
                     
if __name__ == '__main__':
    n=int(input())
    if n > 1022:
        print(-1)
    elif n < 10 :
        print(n)
    else:
        print(solution(n))