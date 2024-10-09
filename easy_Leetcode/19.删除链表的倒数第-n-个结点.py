#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # 方法1：
        # 创建一个虚拟节点，并将下一个指针设置为链表的头部
        dummy_head = ListNode(0, head)

        # 创建两个指针，慢指针和快指针，并将它们初始化为虚拟节点
        slow = fast = dummy_head

        # 快指针比慢指针快 n-1 步
        for i in range(n+1):
            fast = fast.next
        
        # 移动两个指针，直到快指针到达链表的末尾
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 通过更新第 (n-1) 个节点的 next 指针删除第 n 个节点
        slow.next = slow.next.next
        return dummy_head.next


# @lc code=end

