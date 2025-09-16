#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
import collections

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        # 递归法
        # if not root: return 0
        # max_depth = 1
        # for child in root.children:
        #     max_depth = max(max_depth, self.maxDepth(child) + 1)
        #
        # return max_depth


        # 迭代法
        # if not root: return 0
        # 
        # depth = 0
        # queue = collections.deque([root])
        # 
        # while queue:
        #     depth += 1
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         for child in node.children:
        #             queue.append(child)
        # 
        # return depth

        
        # 栈
        if not root: return 0
        max_depth = 0

        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            for child in node.children:
                stack.append((child, depth + 1))
        
        return max_depth
# @lc code=end

