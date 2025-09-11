#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 方法1：暴力
        # n = len(nums)
        # nn = 0
        # for i in range(n):
        #     # 如果这个值不等于val，那么就进行存储
        #     if nums[i] != val:
        #         nums[nn] = nums[i]
        #         nn += 1 
        # # 返回数组的大小
        # return nn
        
        # 方法2：未过？
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] == val:
        #         for j in range(i+1,n):
        #             nums[j-1] = nums[j]
        #         i -= 1
        #         n -= 1
        # # 返回数组的大小
        # return n

        # 方法3：双指针
        # 慢指针
        # slow = 0
        # # 快指针
        # fast = 0
        # # 数组初始长度
        # n = len(nums)
        # for fast in range(n):
        #     if nums[fast] != val:
        #         nums[slow] = nums[fast]
        #         slow += 1
        # return slow

        # 方法4：不知道
        while val in nums:
            nums.remove(val)
        return len(nums)
# @lc code=end

