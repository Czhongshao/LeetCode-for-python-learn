#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 方法1：暴力
        # lens = len(nums)
        # for i in range(lens):
        #     nums[i] = nums[i] ** 2
        # return sort(nums)


        # 方法2: 双指针
        # lens = len(nums)
        # # 左侧指针
        # left = 0
        # # 右侧指针
        # right = lens-1
        # # 排序
        # i = lens - 1
        # # 定义列表,用于存放结果
        # res = [float('inf')] * lens
        # while left <= right:
        #     # 左右边界进行对比,找出最大值
        #     if nums[left] ** 2 < nums[right] ** 2:
        #         res[i] = nums[right] ** 2
        #         # 右指针向左移动
        #         right -= 1
        #     else:
        #         res[i] = nums[left] ** 2
        #         # 左指针向右移动
        #         left += 1
        #     # 排序位置往前移动
        #     i -= 1
        # return res

        # 方法3: 暴力+列表推导
        return sorted(x*x for x in nums)

# @lc code=end

