def comb_sort(arr):

	arr_size = len(arr)
	gap = arr_size
	swapped = False

	while gap > 1 or swapped == True:
		gap = int(gap / 1.3)
		swapped = False
		
		for i in range(arr_size-gap):
			if arr[i] > arr[i+gap]:
				arr[i], arr[i+gap] = arr[i+gap], arr[i]
				sawapped = True	


def main():
	
	arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
	print("Input  : ", arr)
	comb_sort(arr)
	print("Output : ", arr)


if __name__ == '__main__':
	main()
