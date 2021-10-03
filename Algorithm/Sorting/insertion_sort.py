def insertion_sort(arr):

	arr_size = len(arr)

	for i in range(arr_size-1):
		target_id = i+1
		shift_count = 0
		while i - shift_count >= 0:
			if arr[i - shift_count] > arr[target_id - shift_count]:
				arr[i - shift_count], arr[target_id - shift_count] = arr[target_id - shift_count], arr[i - shift_count]
			shift_count = shift_count + 1
           

def main():
    arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
    print("Input  : ", arr)
    insertion_sort(arr)
    print("Output : ", arr)


if __name__ == '__main__':
    main()
