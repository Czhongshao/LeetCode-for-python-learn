#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 如果节点为空，那么就返回True (为空也算对称)
        if not root: return True
        
        # 递归法
    #     return self.compare(root.left, root.right)
    # def compare(self, left, right):
    #     # 首先排除空节点的情况
    #     if left == None and right != None: return False
    #     elif left != None and right == None: return False
    #     elif left == None and right == None: return True
    #     # 排除空节点后，再排除数值不相同的情况
    #     elif left.val != right.val: return False

    #     # 此时，左右节点不为空，且数值相同
    #     # 递归，做下一层判断
    #     outside = self.compare(left.left, right.right) # 左子树：左 ；右子树：右
    #     inside = self.compare(left.right, right.left)
    #     isSame = outside and inside # 左子树：中 ；右子树：中（逻辑处理）
    #     return isSame


        # 迭代法：使用队列
        # queue = collections.deque()
        # queue.append(root.left) # 将左子树头结点加入队列
        # queue.append(root.right) # 将右子树头结点加入队列
        # while queue: # 判断两个数是否相互翻转
        #     leftNode = queue.popleft()
        #     rightNode = queue.popleft()
        #     if not leftNode and not rightNode: # 左节点为空、右节点为空，此时是对称的
        #         continue

        #     # 左右一个节点不为空，或都不为空但数值相同，返回false
        #     if not leftNode or not rightNode or leftNode.val != rightNode.val:
        #         return False
        #     queue.append(leftNode.left) # 加入左节点左孩子
        #     queue.append(rightNode.right) # 加入右节点右孩子
        #     queue.append(leftNode.right) # 加入左节点右孩子
        #     queue.append(rightNode.left) # 加入右节点左孩子
        # return True

        
        # 迭代法：使用栈
        # st = []
        # st.append(root.left)
        # st.append(root.right)
        # while st:
        #     rightNode = st.pop()
        #     leftNode = st.pop()
        #     if not rightNode and not leftNode:
        #         continue
        #     if not leftNode or not rightNode or leftNode.val != rightNode.val:
        #         return False
        #     st.append(leftNode.left)
        #     st.append(rightNode.right)
        #     st.append(leftNode.right)
        #     st.append(rightNode.left)
        # return True


        # 层次遍历
        queue = collections.deque([root.left, root.right])
        while queue:
            level_size = len(queue)

            if level_size % 2 != 0: # 如果为奇数那么必定不是对称的
                return False
            
            level_vals = []
            for i in range(level_size):
                node = queue.popleft()
                if node:
                    level_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_vals.append(None)

            if level_vals != level_vals[::-1]:
                return False
            
        return True

        
# @lc code=end

