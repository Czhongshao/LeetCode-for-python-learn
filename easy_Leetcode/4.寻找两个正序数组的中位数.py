#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 拼接数组，并排序
        nums = sorted(nums1 + nums2)
        # 计算此时长度
        n = len(nums)
        # 找到中位
        mid = n // 2
        # 如果能够整除2，那么 
        if n % 2 == 0:
            return ((nums[mid-1] + nums[mid]) / 2.0)
        else:
            return (nums[mid])
# @lc code=end

