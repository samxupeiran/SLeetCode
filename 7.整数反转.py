#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != '-':
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        if -2147483648 < x < 2147483647:
            return x
        else:
            return 0
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-120))
