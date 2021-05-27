def mergeArray(nums1, nums2):
    if nums2:
        i = 0
        k = 0
        while i < len(nums2):
            if nums2[i] < nums1[k]:
                for j in range(len(nums1) - 1, k, -1):
                    nums1[j] = nums1[j - 1]
                nums1[k] = nums2[i]
                i += 1
                k += 1
            elif k > len(nums2):
                nums1[k] = nums2[i]
                i += 1
                k += 1
            else:
                k += 1


def deleteArrayElements(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            if i == 0:
                nums = nums[1:]
                i += 1
            elif i == len(nums)-1:
                nums = nums[:len(nums) - 1]
            else:
                for k in range(i, len(nums)-1):
                    nums[k] = nums[k + 1]
                nums = nums[:len(nums) - 1]
        else:
            i += 1
    return len(nums), nums


if __name__ == '__main__':
    # nums1 = [-1,0,0,3,3,3,0,0,0]
    # nums2 = [1,2,2]
    # mergeArray(nums1, nums2)
    # nums1 = [1, 2, 3, 0, 0, 0]
    # nums2 = [2, 5, 6]
    nums = [3,2,2,3]
    val = 3
    length, nums = deleteArrayElements(nums, val)
    print(length)
    print(nums)