#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 方法1：递归，swapPairs函数没搜到准确的用法
        # if head is None or head.next is None: return head
        # # 需要反转的两个node分别是pre和cur
        # pre = head
        # cur = head.next
        # next = head.next.next
        # # 后一个节点赋予前一个内容
        # cur.next = pre
        # # 前一个节点赋予后一个节点内容
        # pre.next = self.swapPairs(next)
        # return cur

        # 方法2：迭代，
        dummy_head = ListNode(next=head)
        current = dummy_head

        # 必须有cur的下一个和下下个的时候才能进行交换
        while current.next and current.next.next:
            # 当前要交换的第一个节点
            temp = current.next # 防止节点修改
            # 交换后第一个节点的下一个节点
            temp1 = current.next.next.next

            # 下一个节点内容赋给上一个节点
            current.next = current.next.next
            # 交换
            current.next.next = temp
            # 下下个节点赋给第一个节点位置
            temp.next = temp1
            # 移动current到下一对交换节点位置
            current = current.next.next
        return dummy_head.next


# @lc code=end

