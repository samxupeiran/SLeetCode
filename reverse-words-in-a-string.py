# coding: utf-8

# @Author: peiran.xu


class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("the sky is blue"))
