#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        # 方法2：字典
        mapping = {
            '(':')',
            '[':']',
            '{':'}'
        }

        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()

        return True if not stack else False


        # 方法1：仅使用栈
        # for item in s:
        #     if item == '(':
        #         stack.append(')')
        #     elif item == '[':
        #         stack.append(']')
        #     elif item == '{':
        #         stack.append('}')
        #     elif not stack or stack[-1] != item:
        #         return False
        #     else:
        #         stack.pop()
        # return True if not stack else False

# @lc code=end

