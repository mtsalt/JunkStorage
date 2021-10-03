def bucket_sort(arr):
	
	max_val = max(arr)

	bucket_list = [None] * max_val

	for val in arr:
		bucket_list[val-1] = val

	sorted_arr = []
	for val in bucket_list:
		if val is not None:
			sorted_arr.append(val)

	return sorted_arr

def main():
	arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
	sorted_arr = bucket_sort(arr)
	print("Input  : ", arr)
	print("Output : ", sorted_arr)


if __name__ == '__main__':
	main()
