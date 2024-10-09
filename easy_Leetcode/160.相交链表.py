#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 方法1：求长度，同时出发
        # # 计算链表长度
        # lena, lenb = 0, 0
        # cur = headA
        # while cur:
        #     cur = cur.next
        #     lena += 1
        # cur = headB
        # while cur:
        #     cur = cur.next
        #     lenb += 1
        # # 创建链表a,b
        # cura, curb = headA, headB
        # if lena > lenb: # 让curb 为最长链表的头，lenb为其长度
        #     cura, curb = curb, cura
        #     lena, lenb = lenb, lena
        # # 让cura, curb 在同一个起点(末尾对齐)
        # for _ in range(lenb - lena):
        #     curb = curb.next
        # # 同时遍历cura 和 curb，如果有相同那么就返回
        # while cura:
        #     if cura == curb:
        #         return cura
        #     else:
        #         # 不满足就移动到下一个节点进行判断
        #         cura = cura.next
        #         curb = curb.next
        # return None
    
        # 方法2：等比例法
        # 处理边缘情况
        if not headA or not headB:
            return None
        
        # 在每个链表的头部初始化两个指针
        pointerA = headA
        pointerB = headB

        # 遍历两个链表直到指针相交
        while pointerA != pointerB:
            # 将指针向前移动一个节点 
            # 只要pointer 还存在，那就移动到当前节点的下一节点；反之开始遍历另一个链表
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # 如果相交，指针将位于交点节点，如果没有交点，值为None
        return pointerA


# @lc code=end

