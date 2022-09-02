li,li_tmp = [],[]
for _ in range(int(input())) :
    tmp = input()
    li.append((len(tmp),tmp))

li = list(set(li))

li.sort(key = lambda x: (x[0],x[1]))
for i in li :
    print(i[1])


