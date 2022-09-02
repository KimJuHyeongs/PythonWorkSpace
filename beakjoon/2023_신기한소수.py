import sys
import math
input = sys.stdin.readline

N = int(input())
number = ['1','3','7','9']
def isprime(p):
    for i in range(2,int(math.sqrt(p))):
        if p%i == 0:
            return False
    return True

def make_prime(prime):
    if len(prime) == N:
        print(prime)
        return
    for i in number:
        if isprime(int(prime+i)):
            make_prime(prime+i)
        
start = ['2','3','5','7']
for i in start:
    make_prime(i)