#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 最小深度是从根节点到最近叶子节点的最短路径上的节点数量
        
        # 递归法
        return self.getDepth(root)
        
    def getDepth(self, node):
        if not node: return 0
        leftDepth = self.getDepth(node.left) # 左
        rightDepth = self.getDepth(node.right) # 右

        # 当一个左子树为空，右不为空，此时并不是最低点
        if node.right is not None and node.left is None:
            return 1 + rightDepth
        
        # 当一个右子树为空，左不为空，此时并不是最低点
        if node.left is not None and node.right is None:
            return 1 + leftDepth
        
        result = 1+ min(leftDepth, rightDepth)
        return result
    



        
# @lc code=end

