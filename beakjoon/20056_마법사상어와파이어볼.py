# 위치 = r,c  , 질량 = m,  방향 = d, 속력 = s 
# 마지막 행과 행 연결, 열과 열 연결 
# 8 방향

import sys
from collections import defaultdict
input= sys.stdin.readline

if __name__ == '__main__':
    # 격자, 볼 수, 반복 횟수
    N,M,K = map(int,input().split())
    px, py = [N-1,N-1,0,1,1,1,0,N-1], [0,1,1,1,0,N-1,N-1,N-1]
    # r, c, m, s, d = 행, 열, 질량, 속력, 방향
    fireball = defaultdict(list)
    for i in range(M):
        r,c,m,s,d = map(int,input().split())
        fireball[(r-1,c-1)].append([m,s,d])
    
    for _ in range(K):
        # #이동
        tmp_fireball = defaultdict(list)
        for tx,ty in fireball.keys():
            for tm, ts, td in fireball[(tx,ty)]:
                cx, cy = (tx+(px[td]*ts))%N, (ty+(py[td]*ts))%N
                tmp_fireball[(cx,cy)].append([tm,ts,td])
        
        # 중복 제거
        fireball.clear()
        for key in tmp_fireball.keys():
            if len(tmp_fireball[key]) >= 2:
                sm, ss, sd, cnt = 0,0,[], len(tmp_fireball[key])
                for tm, ts, td in tmp_fireball[key]:
                    sm, ss = sm+tm, ss + ts
                    if td%2 == 0:
                        sd.append(1)
                sm, ss = sm//5, ss//cnt
                if sm == 0 : continue

                if len(sd) == cnt or len(sd) == 0:
                    sd = [0,2,4,6]
                else :
                    sd = [1,3,5,7]
                
                for tmp in sd:
                    fireball[key].append([sm,ss,tmp])
            else :
                fireball[key].extend(tmp_fireball[key])

    result = 0
    for key in fireball.keys():
        for tmp in fireball[key]:
            result += tmp[0]
    print(result)