#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
# import sys
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 方法1：暴力求解
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # 方法2：双指针
        # nums_sorted = sorted(nums)
        # left = 0 
        # right = len(nums) - 1
        # while left < right:
        #     current_sum = nums_sorted[left] + nums_sorted[right]
        #     if current_sum == target:
        #         # 如果和等于目标数，则返回两个数的下标
        #         # 找到nums中的真实下标
        #         left_index = nums.index(nums_sorted[left])
        #         right_index = nums.index(nums_sorted[right])
        #         if left_index == right_index:
        #             right_index = nums[left_index+1:].index(nums_sorted[right]) + left_index + 1
        #         return [left_index, right_index]
        #     elif current_sum < target:
        #         # 如果总和小于目标，则将左侧指针向右移动
        #         left += 1
        #     else:
        #         # 如果总和大于目标值，则将右指针向左移动
        #         right -= 1

        # 方法3：字典
        # records = dict()
        # for index, value in enumerate(nums):
        #     if target - value in records: # 遍历当前元素，在map当中寻找是否有匹配的key
        #         return [records[target - value], index]
        #     records[value] = index
        # return []
    

        # 方法4：使用集合
        # 创建一个集合来存储我们目前看到的数字
        seen = set()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)


# @lc code=end


