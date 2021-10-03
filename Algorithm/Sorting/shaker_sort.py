def shaker_sort(arr):
	
	left_most = 0
	right_most = len(arr) - 1
	
	for i in range(left_most, right_most):
		if arr[i] > arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
	right_most -= 1

	for i in range(right_most, left_most, -1):
		if arr[i-1] > arr[i]:
			arr[i-1], arr[i] = arr[i], arr[i-1]
	left_most -= 1

if __name__ == '__main__':
	
	arr = [5, 2, 1, 4, 3]
	print(arr)
	shaker_sort(arr)
	print(arr)
