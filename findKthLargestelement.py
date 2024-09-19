def findKthLargest(nums, k):
    k = len(nums) - k

    def quickSelect(l, r):
        pivot, p = nums[r], l

        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        nums[r], nums[p] = nums[p], nums[r]

        if p < k:
            return quickSelect(p + 1, r)
        elif p > k:
            return quickSelect(l, p - 1)
        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1)

print(findKthLargest([2, 3, 1, 5, 4], 2))