def binarySearch(arr, key):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = int(start + (end - start) / 2)
        if (key == arr[mid]):
            return mid
        if (key < arr[mid]):
            end = mid - 1
        if (key > arr[mid]):
            start = mid + 1

    return -1


print(binarySearch([1, 2, 3, 4, 5], 1))
