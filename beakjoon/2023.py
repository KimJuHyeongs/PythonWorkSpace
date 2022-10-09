import math

def is_prime(v) :
    for idx in range(2,int(math.sqrt(v))) :
        if v % idx == 0 :
            return False
        
    return True

def make_prime(v) :
    if len(v) == n :
        print(v)
        return
    
    for num in number :
        tmp_val = v + num
        check = is_prime(int(tmp_val))

        if check == True :
            make_prime(tmp_val)

if __name__ == '__main__' :
    n = int(input())
    number = ['1', '3', '7', '9']

    for val in ['2', '3', '5', '7'] :
        make_prime(val)