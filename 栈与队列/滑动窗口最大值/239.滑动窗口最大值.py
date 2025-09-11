#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque() # 这里需要使用deque实现单调队列，直接使用list会超时
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft() # list.pop()时间复杂度为O(n),这里需要使用collections.deque()

    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于队列入口数值
    # 这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    # 查询当前队列里的最大值 直接返回队列前端也就是front就可以了
    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k):
            que.push(nums[i])
        result.append(que.front()) # result 记录前k的元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i - k]) # 滑动窗口移除最前面元素
            que.push(nums[i]) # 滑动窗口前加入最后面的元素
            result.append(que.front()) # 记录对应的最大值
        return result

# @lc code=end

