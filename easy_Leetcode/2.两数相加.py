#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 简化链表，构建哑节点，当第一个节点不为0时如下
        dummy_head = ListNode(0)
        # 构建结果链表
        current = dummy_head
        # 存储进位
        carry = 0

        # 遍历完成两个链表,是否有进位
        while l1 or l2 or carry:
            # 三元运算符，if后面条件为True，则选择前一个赋值；为False，则选择后一个赋值
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # 求得此位和
            sum = v1 + v2 + carry
            # 求得进位数
            carry = sum // 10
            # 存储
            current.next = ListNode(sum % 10)
            # 检查l1,l2此时是否还存在（是否还有下一位）
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            # 移动到下一位
            current = current.next

        return dummy_head.next
# @lc code=end

