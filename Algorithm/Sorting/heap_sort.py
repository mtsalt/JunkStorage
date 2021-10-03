def heap_sort(arr):

    arr_size = len(arr)

    i = 0
    while(i < arr_size):
        upheap(arr, i)
        i += 1

    while(i > 1):
        i -= 1
        tmp = arr[0]
        arr[0] = arr[i]
        arr[i] = tmp

        downheap(arr, i-1)

def upheap(arr, num):
    while num != 0:
        parent = int((num - 1) / 2)
        if arr[num] > arr[parent]:
            tmp = arr[num]
            arr[num] = arr[parent]
            arr[parent] = tmp
            num = parent
        else:
            break

def downheap(arr, num):
    if num == 0:
        return

    parent = 0
    while True:
        child = 2 * parent + 1
        if child > num: break
        if (child < num) and arr[child] < arr[child + 1]:
            child += 1
        if arr[parent] < arr[child]:
            tmp = arr[child]
            arr[child] = arr[parent]
            arr[parent] = tmp
            parent = child
        else:
            break

def main():
    arr = [3, 5, 1, 6, 8, 7, 9, 2, 4]
    print("Input  : ", arr) 
    heap_sort(arr)
    print("Output : ", arr)

if __name__ == "__main__":
    main()