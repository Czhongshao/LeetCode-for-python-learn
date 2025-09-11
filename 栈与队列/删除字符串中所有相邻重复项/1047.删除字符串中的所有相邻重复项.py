#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        # 方法1：栈
        # res = list()
        # for item in s:
        #     if res and res[-1] == item:
        #         res.pop()
        #     else:
        #         res.append(item)
        # return "".join(res) # 字符串拼接

        # 方法2：双指针模拟栈
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 直接换，会把后面的填在slow 的位置
            res[slow] = res[fast]
            
            # 如果发现和前一个一样，那就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1

        return ''.join(res[0: slow])


# @lc code=end

