#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        nums = 0
        fast = 0
        slow = 0
        while fast >= slow:
            # 确保不超过数组长度
            if fast < n:
                # 如果当前位置是空格，那么就把慢指针移动到快指针之后的位置
                if s[fast] == ' ':
                    slow = fast + 1
                else:
                    # 如果当前位置不是空格，那么就计算此刻的长度
                    nums = fast - slow + 1
                # 移动快指针
                fast += 1
            else:
                # 如果超过了数组长度就跳出循环
                break
        return nums

# @lc code=end

