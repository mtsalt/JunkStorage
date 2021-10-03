def radix_sort(arr):

	max_num = max(arr)
	num_of_digits = len(str(max_num))
	for i in range(num_of_digits):
		exp = 10**i
		counting_sort(arr, exp)

def counting_sort(arr, exp):
	
	max_num = max(arr)
	cp_arr = arr.copy()

	count = [0 for _ in range(max_num+1)]
	for num in cp_arr:
		count[num] += 1

	for i in range(len(count)-1):
		count[i+1] += count[i]

	result = [0 for _ in range(len(arr))]
	for num in cp_arr:
		id_num = count[num]
		arr[id_num-1] = num	
		count[num] -= 1

if __name__ == '__main__':
	arr = [53, 89, 150, 300, 36, 33, 233]
	print("Input  : ", arr)
	radix_sort(arr)
	print("Output : ", arr)






