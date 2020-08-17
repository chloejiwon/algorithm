def insertionsort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        tmp = arr[i]
        p = i
        for j in reversed(range(i)):
            if arr[j] >= tmp:
                arr[j+1] = arr[j]
                p = j
            else :
                break
        
        arr[p] = tmp
        print(arr)
    return arr


arr = [8,5,6,2,4]
arr = insertionsort(arr)
print 'sorted array : ', arr