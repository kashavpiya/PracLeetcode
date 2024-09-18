def mergeSort(arr):
    if len(arr) > 1:
        l = arr[:len(arr)//2]
        r = arr[len(arr)//2:]
        mergeSort(l)
        mergeSort(r)
        merge(arr, l, r)

def merge(arr, l, r):
    i = 0
    j = 0
    k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        k += 1
        i += 1

    while j < len(r):
        arr[k] = r[j]
        k += 1
        j += 1

arr = [2, 4, 8, 6, 1, 3, 9, 5]
mergeSort(arr)
print(arr)

