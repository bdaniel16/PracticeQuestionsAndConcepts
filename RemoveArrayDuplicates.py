from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    [0,1,2,3,4,2,2,3,3,4]
    [1,2,2]
    """
    if not nums:
        return 0
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            nums[i + 1] = nums[j]
            j += 1
            i += 1
    nums = nums[:i + 1]
    return len(nums)


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))