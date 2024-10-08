def productExceptSelf(nums):
    prefix, postfix = 1, 1
    res = [1] * len(nums)

    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

def main():
    print(productExceptSelf([1, 2, 3, 4]))

if __name__ == "__main__":
    main()
