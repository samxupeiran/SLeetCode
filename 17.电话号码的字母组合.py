#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        conversion = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        product = ['']
        for k in digits:
            product = [i + j for i in product for j in conversion[k]]
        return product
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations('23'))
