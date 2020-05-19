#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rdx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[rdx] = nums[i]
                rdx += 1
        return rdx
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([3, 2, 2, 3], 3))
