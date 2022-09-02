import sys
import copy
input = sys.stdin.readline

def del_zero(tmp_l):
    global one_matrix

    for _ in range(tmp_l):
        one_matrix.remove(0)
        one_matrix.append(0)

if __name__ == '__main__':
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    mgs = [list(map(int,input().split())) for _ in range(M)]
    length, one_matrix = N*N, [-1]
    tx,ty,x,y,td,time = [0,1,0,-1],[-1,0,1,0],N//2, N//2,-1,0
    px,py = [-1,1,0,0],[0,0,-1,1]
    position_index = [(N//2,N//2-1)]
    # 1차원으로 변환
    for i in range(2*N-2):
        td = i%4
        if td == 0 or td == 2:
            time += 1
        for t in range(time) :
            cx,cy = x+tx[td],y+ty[td]
            one_matrix.append(matrix[cx][cy])
            position_index.append((cx,cy))
            x,y = cx,cy
    for i in range(N-2,-1,-1):
        one_matrix.append(matrix[0][i])
        position_index.append((0,i))
    # 방향
    result = [0,0,0,0]
    for mg in mgs:
        #skill
        p_cnt,tx,ty,x,y = 0,px[mg[0]-1],py[mg[0]-1],N//2,N//2
        for i in range(1,mg[1]+1):
            cx,cy = x+(tx*i), y+(ty*i)
            idx = position_index.index((cx,cy))
            one_matrix[idx] = 0
            p_cnt += 1
        #제거
        del_zero(p_cnt)
        
        #폭발
        while True:
            cnt,tmp_result = 1,[0,0,0,0]
            for idx in range(1,N*N-1):
                if one_matrix[idx] == one_matrix[idx+1]:
                    cnt+=1
                    if idx+1 == N*N-1:
                        if cnt >= 4:
                            tmp_result[one_matrix[idx]] += cnt
                            for i in range(idx+2-cnt,idx+2):
                                one_matrix[i] = 0
                        break
                else :
                    if cnt >= 4:
                        tmp_result[one_matrix[idx]] += cnt
                        for i in range(idx+1-cnt,idx+1):
                                one_matrix[i] = 0
                    cnt = 1
                if one_matrix[idx+1] == 0 or idx+1 == N*N:
                        break
            
            #제거
            cur_cnt = sum(tmp_result)
            if cur_cnt == 0:
                break
            del_zero(cur_cnt)
            for i in range(1,4):
                result[i] += tmp_result[i]

        #변화
        tmp_matrix = copy.deepcopy(one_matrix)
        one_matrix.clear()
        one_matrix.append(-1)
        cnt,val,val_cnt = 1,0,1
        for idx in range(1,N*N-1):
            if idx+1 == N*N or tmp_matrix[idx+1] == 0:
                one_matrix.append(cnt)
                one_matrix.append(tmp_matrix[idx])
                break
            elif tmp_matrix[idx] == tmp_matrix[idx+1]:
                cnt+=1
            else :
                one_matrix.append(cnt)
                one_matrix.append(tmp_matrix[idx])
                val_cnt += 2
                cnt = 1
                if val_cnt == N*N:
                    break

        if len(one_matrix) == 1:
            break
        if len(one_matrix) < N*N:
            one_matrix += [0]*((N*N)-len(one_matrix))
    
    total = 0
    for i in range(1,4):
        total += i * result[i]
    print(total)