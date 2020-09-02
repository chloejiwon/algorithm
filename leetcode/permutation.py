def perm(list, start):
    if start == len(list)-1:
        #print("before append = ", perm_list)
        temp  = []
        for i in range(len(list)):
            temp += list[i]
        perm_list.append(temp)
        #print(list)
        #print("perm_list = ", perm_list)
        return
    for i in range(start, len(list)):
        list[start], list[i] = list[i], list[start]
        perm(list, start+1)
        list[start],list[i] = list[i],list[start]
    

perm_list = []
perm([1,2,3,4],0)
print(perm_list)