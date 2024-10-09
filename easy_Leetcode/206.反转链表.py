#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 方法1：双指针法
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        # cur = head
        # pre = None
        # while cur:
        #     tmp = cur.next # 保存 cur 的下一个节点，之后要改变指向cur->next
        #     cur.next = pre # 反转
        #     # 更新pre、cur指针
        #     pre = cur
        #     cur = tmp
        # return pre

        # 方法2：递归
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not head or not head.next: return head
        # 反转列表剩余部分
        pre = self.reverseList(head.next)
        # 修改指针指向
        head.next.next = head
        # 断开之间的链接
        head.next = None
        return pre


# @lc code=end

