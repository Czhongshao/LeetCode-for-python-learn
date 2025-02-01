#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return []

        queue = collections.deque([root])
        averages = []

        while queue:
            size = len(queue)
            level_sum = 0

            for i in range(size):
                node = queue.popleft()

                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            averages.append(level_sum / size)
        
        return averages

# @lc code=end

