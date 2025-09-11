#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 方法1
        # if not root:
        #     return []
        
        # result = []
        # queue = collections.deque([root])

        # while queue:
        #     level_size = len(queue)
        #     level = []

        #     for _ in range(level_size):
        #         node = queue.popleft()
        #         level.append(node.val)

        #         for child in node.children:
        #             queue.append(child)

        #     result.append(level)
        # return result


        # 方法2：递归法1
        # if not root:
        #     return []
        # result = []

        # def traversal(root, depth):
        #     if len(result) == depth:
        #         result.append([])

        #     result[depth].append(root.val)

        #     if root.children:
        #         for i in range(len(root.children)):
        #             traversal(root.children[i], depth+1)

        # traversal(root, 0)
        # return result
        
        # 方法3：递归法2

        if not root:
            return []
        result = []

        def traversal(root, depth):
            if len(result) == depth:
                result.append([])
            result[depth].append(root.val)
            
            for child in root.children:
                traversal(child, depth + 1)

        traversal(root, 0)
        return result

        
# @lc code=end

