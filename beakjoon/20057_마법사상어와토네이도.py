# 밖으로 나간 모래의 양
import sys
from collections import defaultdict
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    px, py, cnt = [0,1,0,-1], [-1,0,1,0], [2]*N
    cnt[-1] = 3

    rotate = defaultdict(list)
    left = [(-2,0,0.02),(-1,-1,0.1),(-1,0,0.07),(-1,1,0.01),(1,-1,0.1),
            (1,0,0.07),(1,1,0.01),(2,0,0.02),(0,-2,0.05),(0,-1,-1)]
    rotate[0].extend(left)
    rotate[1].extend([(-y,x,z) for x,y,z in left])
    rotate[2].extend([(x,-y,z) for x,y,z in left])
    rotate[3].extend([(y,x,z) for x,y,z in left])

    cx, cy, d = N//2, N//2, 0
    result = 0
    for i in range(1,N):
        #확산
        for _ in range(cnt[i]):
            for _ in range(i):
                cx,cy = cx+px[d], cy+py[d]
                tmp = 0
                for tx,ty,tz in rotate[d]:
                    xx,yy,val = cx+tx, cy+ty,0
                    if tz == -1 :
                        val = matrix[cx][cy] - tmp
                    else :
                        val = int(matrix[cx][cy]*tz)
                        tmp += val

                    if 0<=xx<N and 0<=yy<N :
                        matrix[xx][yy] += val
                    else :
                        result += val
            d = (d+1)%4
    print(result)









    # for i in range(2*N-1):
    #     d = i%4
    #     if d == 0 or d==2 : cnt+=1
    #     #확산
    #     for _ in range(cnt):
    #         x,y = cx+px[d], cy+py[d]
    #         tmp = 0
    #         for tx,ty,tz in rotate[d]:
    #             xx,yy = x+tx, y+ty
    #             if tz != -1:
    #                 val = int(matrix[x][y]*tz)
    #                 tmp += val
    #                 if 0<=xx<N and 0<=yy<N :
    #                     matrix[xx][yy] += val
    #                 else :
    #                     result += val
    #             else :
    #                 if 0<=xx<N and 0<=yy<N :
    #                     matrix[xx][yy] += matrix[x][y] - tmp
    #                 else :
    #                     result += matrix[x][y] - tmp
