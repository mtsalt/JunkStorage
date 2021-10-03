def shell_sort(arr):
	
	arr_size = len(arr)
	
	gaps = [pow(2, i)-1 for i in range(arr_size) if pow(2, i)-1 < arr_size and i != 0]
	gaps.reverse()

	for gap in gaps:
		for i in range(arr_size - gap):
			
			target_id = i + gap
			shift_count = 0
			while i >= 0:
				if arr[i] > arr[target_id]:
					arr[i], arr[target_id] = arr[target_id], arr[i]
				shift_count = shift_count + 1
				target_id = target_id - shift_count * gap
				i = i - shift_count


def main():
	arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
	print("Input  : ", arr)
	shell_sort(arr)
	print("Output : ", arr)


if __name__ == '__main__':
	main()
	
	
	
	
