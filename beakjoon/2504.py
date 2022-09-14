import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__' :
    string = deque(input().rstrip())
    string.reverse()

    q, result = deque(), 0

    while (string) :
        tmp = string.pop()
        
        if tmp == ')' :
            if not q :
                print(0)
                exit(0)
                
            val = 0

            while (q) :
                ttmp = q.pop()

                if ttmp == '(' :
                    if val == 0 :
                        q.append(2)
                    else :
                        q.append(val*2)
                    break

                elif ttmp == '[' :
                    print(0)
                    exit(0)
                
                else :
                    val += ttmp

        elif tmp == ']' :
            if not q :
                print(0)
                exit(0)

            val = 0

            while (q) :
                ttmp = q.pop()

                if ttmp == '[' :
                    if val == 0 :
                        q.append(3)
                    else :
                        q.append(val*3)
                    break

                elif ttmp == '(' :
                    print(0)
                    exit(0)
                
                else :
                    val += ttmp
        
        else :
            q.append(tmp)

    for v in q :
        if type(v) == int :
            result += v
        else :
            print(0)
            exit(0)
    
    print(result)
