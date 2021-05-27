from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    [1,2,3,0,0,0], [2,5,6]
        p1     p        p2
    """
    p1 = m-1
    p2 = n-1
    p = m+n-1
    while p >= 0:
        if p2 < 0:
            break
        elif p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


if __name__ == "__main__":
    nums1 = [2,0]
    nums2 = [1]
    merge(nums1, 1, nums2, 1)
    print(nums1)