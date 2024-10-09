#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 方法1：快慢指针法
        # fast = head
        # slow = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         # 给slow 指针重新赋原链表
        #         slow = head
        #         # 一直循环到两者相等的时候
        #         while slow != fast:
        #             slow = slow.next
        #             fast = fast.next
        #         return slow
        # return None

        # 方法2：集合法
        # 建立一个空集合
        visited = set()
        # 只要链表非NULL就继续执行
        while head:
            # 如果链表中的某节点出现在visited当中，就返回当前链表
            if head in visited:
                return head
            # 集合添加当前的节点
            visited.add(head)
            head = head.next
        return None

# @lc code=end

