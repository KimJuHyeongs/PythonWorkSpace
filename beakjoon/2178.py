from collections import deque

if __name__ == '__main__' :
    n, m = map(int,input().split())
    matrix, q = list(), deque()
    px, py = [1,0,-1,0],[0,1,0,-1]
    q.append([0,0,1])

    for _  in range(n) :
        matrix.append(list(map(int,input())))
    matrix[0][0] = 0
    
    while q :
        x, y, depth = q.popleft()

        for idx in range(4) :
            tx, ty = x + px[idx], y + py[idx]
                
            if (0 <= tx < n) and (0 <= ty < m) and matrix[tx][ty] == 1 :
                if (tx == n-1) and (ty == m-1) :
                    print(depth + 1)
                    exit(0)
                else :
                    matrix[tx][ty] = 0
                    q.append([tx,ty,depth+1])
                    