import sys
input = sys.stdin.readline
n = int(input())
tree = {}
for _ in range(n):
    cur, left, right = input().split()
    tree[cur] = {'left' : left, 'right' : right}

def pre_order(c):
    l, r = tree[c]['left'], tree[c]['right']
    print(c,end='')
    if l != '.':
        pre_order(l)
    if r != '.':
        pre_order(r)

def in_order(c):
    l, r = tree[c]['left'], tree[c]['right']
    if l != '.':
        in_order(l)
    print(c,end='')
    if r != '.':
        in_order(r)

def post_order(c):
    l, r = tree[c]['left'], tree[c]['right']
    if l != '.':
        post_order(l)
    if r != '.':
        post_order(r)
    print(c,end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()
