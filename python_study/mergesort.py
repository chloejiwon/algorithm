########## merge sort ##############
# Time Complexity : O(nlogn)
###################################
def merge(left, right):
    arr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            arr.append(left[0])
            left = left[1:]
        elif left[0] > right[0]:
            arr.append(right[0])
            right = right[1:]
        else :
            arr.append(left[0])
            arr.append(right[0])
            left, right = left[1:], right[1:]

    if len(left) > 0 and len(right) == 0:
        arr = arr + left
    if len(left) ==0 and len(right) >0 :
        arr = arr + right

    return arr

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftarr = arr[:mid]
    rightarr = arr[mid:]
    leftarr = mergesort(leftarr)
    rightarr = mergesort(rightarr)
    return merge(leftarr, rightarr)

arr = [8,5,6,2,4]
arr = mergesort(arr)
print 'sorted array : ', arr