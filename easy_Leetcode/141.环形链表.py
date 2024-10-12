#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 方法1：快慢指针法
        fast = head
        slow = head
        # 只要快指针和快指针的下一个不为NULL就继续循环
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            # 快指针出现过等于慢指针的情况，返回True
            if fast == slow:
                return True
        # 如果始终没有追上，那么就返回False
        return False
        
# @lc code=end

