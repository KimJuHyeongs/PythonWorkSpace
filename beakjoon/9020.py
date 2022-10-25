# def is_prime(v) :
#     for i in range(2,v) :
#         if v % i == 0 :
#             return False
    
#     return True

# if __name__ == '__main__' :
#     testcase = int(input())
#     li = [int(input()) for _ in range(testcase)]
    
#     max_val = max(li)
#     prime = [False]*(max_val+1)
#     result = []
    
#     for idx in range(2,len(prime)):
#         prime[idx] = is_prime(idx)
    
#     for val in li :
#         pass_check = False
#         half_val = int(val/2)
        
#         for first in range(half_val, 1, -1) :
#             if not prime[first] :
#                 continue
            
#             for second in range(half_val+(half_val-first),1,-1) :
#                 if not prime[second] :
#                     continue
                
#                 if first + second == val :
#                     result.append([first,second])
#                     pass_check = True
#                     break
            
#             if pass_check :
#                 break
                    
#     for f, s in result :
#         print(f,s)

if __name__ == '__main__' :
    testcase = int(input())
    max_number = 10001
    prime = [0]*max_number
    
    for idx in range(2,max_number) :
        prime[idx] = idx
        
    for idx in range(2,max_number) :
        if prime[idx] == 0:
            continue
        
        for idx2 in range(idx+idx,max_number,idx) :
            prime[idx2] = 0
            
    for _ in range(testcase) :
        val = int(input())
        
        for i in range(int(val/2),val+1) :
            if prime[i] and prime[val-i] :
                print(val-i, i)
                break