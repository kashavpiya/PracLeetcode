def twoSum(list1, target):
    #brute force
    for i in range(len(list1)):
        for j in range(1, len(list1)):
            if list1[i] + list1[j] == target:
                return (i, j)
    return (0)

    #using dictionaries
    dict1 = {}

    for i, n in enumerate(list1):
        diff = target - n
        if diff in dict1:
            return (dict1[diff], i)
        dict1[n] = i



def main():
    print(twoSum([4, 2, 1, 5], 3))

if __name__ == "__main__":
    main()