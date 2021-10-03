def gnome_sort(arr):

    arr_size = len(arr)

    i = 0
    while i < arr_size-1:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            if i > 0:
                i -= 1
        else:
            i += 1
    return arr

def main():
    arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
    print("Input  : ", arr) 
    sorted_arr = gnome_sort(arr)
    print("Output : ", sorted_arr)

if __name__ == '__main__':
    main()