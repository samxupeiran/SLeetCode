#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#


# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        print(nums1, nums2)
        n1, n2 = len(nums1), len(nums2)

        # # compare versions
        # for i in range(max(n1, n2)):
        #     i1 = int(nums1[i]) if i < n1 else 0
        #     i2 = int(nums2[i]) if i < n2 else 0
        #     if i1 != i2:
        #         return 1 if i1 > i2 else -1

        # # the versions are equal
        # return 0

        # 比较版本
        for i in range(max(n1, n2)):
            if i < n1:
                i1 = int(nums1[i])
            else:
                i1 = 0
            if i < n2:
                i2 = int(nums2[i])
            else:
                i2 = 0
            if i1 != i2:
                if i1 > i2:
                    return 1
                else:
                    return -1
        # 版本相同
        return 0
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion("1.0.1.0", "1.0.1"))
