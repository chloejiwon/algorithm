def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr)/2]
	less_arr,equal_arr, bigger_arr = [], [],[]
	
	for i in range(len(arr)):
		if arr[i] < pivot : 
			less_arr.append(arr[i])
		elif arr[i] > pivot :
			bigger_arr.append(arr[i])
		else :
			equal_arr.append(arr[i])
	return quicksort(less_arr)+equal_arr+quicksort(bigger_arr)	


arr = [1, 3, 2, 7, 0, 9]
print "Befor arr : ", arr
arr = quicksort(arr)
print "After Quicksort: ",arr
