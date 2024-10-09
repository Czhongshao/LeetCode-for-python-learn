#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 定义左右边界
        left,right = 0,len(nums)-1
        result = [-1,-1]
        if len(nums) == 0:
            return result
        # 找到左边界位置
        while left < right:
            middle = (left + right)//2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        # 记录左边界
        if nums[left] != target:
            return result
        else:
            result[0] = left
        # 重新定义右边界
        right = len(nums) - 1
        # 开始寻找右边界
        while left < right:
            middle = (left + right + 1) // 2
            if nums[middle] <= target:
                left = middle
            else:
                right = middle - 1
        result[1] = left
        return result

        # left = 0
        # right = len(nums)-1
        # if len(nums)==0:
        #     return [-1,-1]
        # rel = []
        # while left<right:
        #     mid = (left+right)//2
        #     if nums[mid]<target:
        #         left = mid+1
        #     else:
        #         right = mid
        # if nums[left] != target:
        #     return [-1,-1]
        # else:
        #     rel.append(left)
        # right = len(nums)-1
        # while left<right:
        #     mid = (left+right+1)//2
        #     if nums[mid]<=target:
        #         left = mid
        #     else:
        #         right = mid-1
        # rel.append(left)
        # return rel

# @lc code=end

