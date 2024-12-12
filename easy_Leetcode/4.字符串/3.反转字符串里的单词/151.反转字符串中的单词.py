#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # 方法1
        # s = s.strip()
        # s = s[::-1]
        # s = ' '.join(word[::-1] for word in s.split())
        # return s

        # 方法2：双指针
        words = s.split()
        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return ' '.join(words)


# @lc code=end

