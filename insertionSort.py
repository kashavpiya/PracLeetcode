import random

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

def main():
    arr = [random.randint(0, 100) for i in range(20)]
    print(arr)
    insertionSort(arr)
    print(arr)

if __name__ == "__main__":
    main()