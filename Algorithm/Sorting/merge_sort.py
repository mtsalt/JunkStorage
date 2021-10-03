from random import shuffle

def merge_sort(arr):

	arr_size = len(arr)

	if arr_size <= 1:
		return arr

	middle = arr_size // 2

	left = merge_sort(arr[:middle])
	right = merge_sort(arr[middle:])

	return merge(left, right)

def merge(left, right):
	
	merged_arr = []
	l, r = 0, 0
	while l < len(left) and r < len(right):

		if left[l] <= right[r]:
			merged_arr.append(left[l])
			l += 1
		else:
			merged_arr.append(right[r])
			r += 1
	
	if left:
		merged_arr.extend(left[l:])
	if right:
		merged_arr.extend(right[r:])
		
	return merged_arr

def main():
	arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
	print("Input  : ", arr)
	arr = merge_sort(arr)
	print("Output : ", arr)

if __name__ == '__main__':
    main()
