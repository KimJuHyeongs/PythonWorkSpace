from pickle import TRUE
import sys
input = sys.stdin.readline

if __name__ == '__main__' :
    n, num_k, num_q, num_m = map(int,input().split(' '))
    k = list(map(int, input().split(' ')))
    q = list(map(int, input().split(' ')))

    k_check = [False for _ in range(n+3)]
    check = [1 for _ in range(n+3)]
    check[0], check[1], check[2] = 0, 0, 0

    for kk in k :
        k_check[kk] = True
    
    for qq in q :
        idx = 1
        if k_check[qq] :
            continue
        while qq*idx <= n+2 :
            if not k_check[qq*idx] :
                check[qq*idx] = 0
            idx += 1
    
    for idx in range(3,n+2) :
        check[idx+1] += check[idx] 

    for _ in range(num_m):
        s, e = map(int,input().split(' '))
        print((check[e] - check[s-1]))
    