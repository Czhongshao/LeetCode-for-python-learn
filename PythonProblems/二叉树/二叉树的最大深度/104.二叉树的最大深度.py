#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # 递归法简化版
        # if not root: return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # 递归法
    #     return self.getdepth(root)
    #
    # def getdepth(self, node):
    #     if not node:
    #         return 0
    #     leftheight = self.getdepth(node.left) # 左
    #     rightheight = self.getdepth(node.right) # 右
    #     height = 1 + max(leftheight, rightheight) # 中
    #     return height

        # 层序遍历迭代法
        if not root: return 0

        depth = 0
        queue = collections.deque([root])

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

# @lc code=end

