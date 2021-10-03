def counting_sort(arr):

	min_num = min(arr)
	max_num = max(arr)

	count = [0 for i in range(max_num+1)]
	for num in arr:
		count[num] += 1
	
	for i in range(max_num):
		count[i+1] += count[i]	

	result = [0 for _ in range(len(arr))]
	for num in arr:
		result[count[num]-1] = num
		count[num] -= 1

	return result

if __name__ == '__main__':

	arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
	print("Input  : ", arr)
	sorted_arr = counting_sort(arr)
	print("Output : ", sorted_arr)

