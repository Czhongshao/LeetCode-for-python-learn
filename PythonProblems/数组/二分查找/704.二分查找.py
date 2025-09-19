#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left1 = 0
        right1 = n-1

        while(left1 <= right1):
            middle1 = (left1 + right1)//2
            if nums[middle1] > target:
                right1 = middle1 - 1
            elif nums[middle1] < target:
                left1 = middle1 + 1
            else:
                return middle1
        return -1
# @lc code=end

