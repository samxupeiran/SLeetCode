# coding: utf-8

# @Author: peiran.xu


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, j in enumerate(nums):
            k = i + 1
            if nums[k:].count(target - j) > 0:
                for n in range(nums[k:].count(target - j)):
                    b = nums.index(target - j, k)
                    return (i, b)
                    k = b + 1


if __name__ == "__main__":
    s = Solution()
    s.twoSum([2, 7, 11, 15], 9)
