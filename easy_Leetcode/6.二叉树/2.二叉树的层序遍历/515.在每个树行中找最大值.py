#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        result = []
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            max_val = float('-inf')

            for _ in range(level_size):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(max_val)

        return result

        
# @lc code=end

