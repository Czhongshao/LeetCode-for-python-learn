#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 方法1：暴力，超时了。。。
        # # 计算长度
        # lens = len(nums)
        # length = float('inf')
        # for i in range(lens):
        #     sum = 0
        #     for j in range(i,lens):
        #         sum += nums[j]
        #         if sum >= target:
        #             length = min(length, j - i + 1)
        #             break
        # return length if length != float('inf') else 0

        # 方法2：滑动窗口
        lens = len(nums)
        left = 0
        right = 0
        length = float("inf")
        sum = 0

        while right < lens:
            # 移动右边界，并记录当前范围的总和
            sum += nums[right]
            # 只要当前综合大于等于标记值，就对此时的范围进行记录
            while sum >= target:
                # 选出最优解（最小的范围）
                length = min(length, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        # 如果length不是空的，那么就返回当前数值，反之就返回0
        return length if length != float('inf') else 0

# @lc code=end