# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            k = i + 1
            if nums[k:].count(target - j) > 0:
                for n in range(nums[k:].count(target - j)):
                    b = nums.index(target - j, k)
                    return (i, b)
                    k = b + 1
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
