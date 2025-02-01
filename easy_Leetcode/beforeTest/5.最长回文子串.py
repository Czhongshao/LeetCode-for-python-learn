#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 判断是否为空字符串，并返回空值
        if n == 0:
            return ""
        # 创建二维数组dp,大小为n*n
        dp = [[False] * n for _ in range(n)]
        # 初始化最长回文子串的起始位置和长度
        start = 0
        maxlen = 1
        # 单一字符必定为回文，将dp[i][i] 设置为True
        for i in range(n):
            dp[i][i] = True
        # 遍历字符串，计算dp数组的值
        # 从1开始避免重复检查，比如只有1或者2个字符时
        for j in range(1,n): # 右边界循环
            for i in range(j): # 左边界循环
                if s[i] == s[j]:
                    # 当前字符串的首尾相等，那么去除首尾仍然为回文
                    if j - i + 1 <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        # 更新最长回文子串的起始位置和长度
                        if j - i + 1 > maxlen:
                            maxlen = j - i + 1
                            start = i
        return s[start : start + maxlen]
# @lc code=end