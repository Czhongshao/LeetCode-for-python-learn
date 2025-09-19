#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 如果节点为空那么就返回
        if not root: return None

        # 递归法：前序遍历
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # 迭代法：前序遍历
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return root

        # 递归法：中序遍历
        # self.invertTree(root.left)
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # return root

        # 递归法：伪中序遍历
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node.right:
        #         stack.append(node.right)
        #     node.left, node.right = node.right, node.left # 放到中间，依然是前序遍历
        #     if node.right:
        #         stack.append(node.right)
        # return root  

        # 递归法：后序遍历
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # root.left, root.right = root.right, root.left
        # return root

        # 迭代法：伪后序遍历
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        #     node.left, node.right = node.right, node.left
        # return root

        # 迭代法：广度优先遍历（层序遍历）
        quene = collections.deque([root])
        while quene:
            node = quene.popleft()
            node.left, node.right = node.right, node.left
            if node.left: quene.append(node.left)
            if node.right: quene.append(node.right)
        return root

# @lc code=end

