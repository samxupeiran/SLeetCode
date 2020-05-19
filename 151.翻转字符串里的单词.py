#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue    "))
