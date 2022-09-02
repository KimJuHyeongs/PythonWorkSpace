import sys
input = sys.stdin.readline

def cal_result(s,e,r,max_tmp):
    global result
    for idx,height in enumerate(heights[s:e:r]):
        if max_tmp > height:
            result += min(max_tmp,max_val) - height
        else:
            max_tmp = max(max_tmp,height)

if __name__ == '__main__':
    #세로, 가로
    h,w = map(int,input().split())
    # 0~h
    heights = list(map(int,input().split()))
    result = 0
    max_val = max(heights)
    max_idx = heights.index(max_val)
    #앞~max
    cal_result(1, max_idx, 1, heights[0])
    #뒤~max
    cal_result(w-1, max_idx, -1, heights[-1])

    print(result)
