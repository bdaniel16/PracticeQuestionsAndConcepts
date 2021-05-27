"""
Learnt that python dict does not return anything(empty)
when the value is a 0 (int) so have to convert to str-int
"""


def twoSum(nums, target):
    diff_map = {}
    for i in range(len(nums)):
        if diff_map.get(target - nums[i]):
            return [int(diff_map.get(target - nums[i])), i]
        diff_map[nums[i]] = str(i)
    return []


if __name__ == "__main__":
    nums = [2,7,11,15]
    print(twoSum(nums, 9))