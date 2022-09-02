# import sys
# import copy
# input = sys.stdin.readline

# def cnt_learn(tmp, l):
#     tmp=set(tmp)
#     cnt = 0
#     for t in tmp:
#         if t not in l:
#             cnt += 1
#     return cnt, tuple(sorted(tmp - l))

# def BT(idx,cnt,cur_k,l):
#     global result

#     if cur_k == 0 :
#         result = max(result, cnt)
#     if idx == len(li):
#         return
#     else :
#         tmp, tmp_word = cnt_learn(''.join(li[idx]), l)
#         if tmp == 0:
#             BT(idx+1,cnt+1,cur_k,l)
#             return
#         elif tmp <= k:
#             BT(idx+1,cnt+1,cur_k-tmp,l|set(tmp_word))
#         BT(idx+1,cnt,cur_k,l)

# if __name__ == '__main__':
#     n,k = map(int,input().split())
#     words = [input().rstrip() for _ in range(n)]
#     learn,result = {'a','n','t','i','c'},0
#     if k<5:
#         print(0)
#         exit(0)
#     k -= 5
#     li = []
#     for idx,word in enumerate(words):
#         tmp,tmp_word = cnt_learn(word, learn)
#         if tmp == 0: result += 1
#         elif tmp <= k :
#             li.append(tmp_word)

#     BT(0,result,k,copy.deepcopy(learn))
#     print(result)


import sys
from itertools import combinations
input = sys.stdin.readline

def word_to_bin(tmp):
    global word
    tmp_result = 0
    for t in tmp:
        tmp_result |= (1 << li[t])
    words.append(tmp_result)

if __name__ == '__main__':
    n,k = map(int,input().split())
    learn = {'a','n','t','i','c'}
    li,words,result = dict(),[],0
    for idx,v in enumerate(set(map(chr,range(ord('a'),ord('z')+1) )) - learn):
        li[v] = idx

    for _ in range(n):
        tmp = set(input().rstrip()[4:-4]).difference(learn)
        word_to_bin(tmp)
    if k < 5:
        print(0)
        exit(0)
    
    all_bin = (2**i for i in range(21))
    
    for val in combinations(all_bin, k-5):
        val,cnt = sum(val),0
        for word in words:
            if word & val == word:
                cnt += 1
        result = max(result, cnt)

    print(result)