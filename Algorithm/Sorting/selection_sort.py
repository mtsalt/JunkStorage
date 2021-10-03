def selection_sort(arr):

    arr = arr[:]
    for i in range(len(arr) - 1):
        index_num = min_index(arr[i:])
        if index_num != i:
            tmp = arr[i]
            arr[i] = arr[index_num + i]
            arr[index_num + i] = tmp
    
    return arr

def min_index(arr):
    min_value = arr[0]
    min_id = 0
    for i in range(len(arr)-1):
        if min_value > arr[i+1]:
            min_value = arr[i+1]
            min_id = i+1 
    return min_id

def main():
    arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
    sorted_arr = selection_sort(arr)
    print("Input  : ", arr) 
    print("Output : ", sorted_arr)
    
if __name__ == '__main__':
    main()
