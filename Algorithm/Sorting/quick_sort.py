def quick_sort(arr):
    arr_size = len(arr)

    if arr_size <= 1:
        return arr

    middle = arr[int(arr_size / 2)]
    
    left = []
    right = []
    for num in arr:
        if num < middle:
            left.append(num)
        elif middle < num:
            right.append(num)
    
    left = quick_sort(left)
    right = quick_sort(right)

    return left + [middle] + right

def main():
    arr = [4, 2, 5, 6, 3, 1, 8, 9, 7]
    sorted_arr = quick_sort(arr)
    print("Input  : ", arr)
    print("Output ; ", sorted_arr)


if __name__ == '__main__':
    main()
