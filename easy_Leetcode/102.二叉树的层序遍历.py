#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # 方法1：长度法
        # if not root:
        #     return []
        # queue = collections.deque([root])
        # result = []
        # while queue:
        #     level = []
        #     for _ in range(len(queue)):
        #         cur = queue.popleft()
        #         level.append(cur.val)
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        #     result.append(level)
        # return result


        # 方法2：递归法
        if not root:
            return []
        levels = []

        def traverse(node, level):
            if not node:
                return 
            
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 0)
        return levels

# @lc code=end

