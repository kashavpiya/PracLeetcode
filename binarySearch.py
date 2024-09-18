def binarySearch(arr, ele):
    a, b = 0, len(arr) - 1

    while b >= a:
        x = int((a+b)/2)
        if arr[x] < ele:
            a = x + 1
        elif arr[x] > ele:
            b = x - 1
        else:
            return x
    return None

print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 7))


#binarySearch works only on a sorted list