#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ...
        # 方法1：暴力
        # m, n = len(haystack), len(needle)
        # for i in range(m):
        #     if haystack[i: i+n] == needle:
        #         return i
        # return -1

        # 方法3：find
        return haystack.find(needle)

        # 方法2：前缀表减1
        # if not needle:
        #     return 0
        # next = [0] * len(needle)
        # self.getNext(next, needle)
        # j = -1
        # for i in range(len(haystack)):
        #     while j >= 0 and haystack[i] != needle[j+1]:
        #         j = next[j]
        #     if haystack[i] == needle[j+1]:
        #         j += 1
        #     if j == len(needle) - 1:
        #         return i - len(needle) + 1
        # return -1    

    # 方法2：前缀表减1
    # def getNext(self, next, s):
    #     j = -1
    #     next[0] = j
    #     for i in range(1, len(s)):
    #         while j >= 0 and s[i] != s[j+1]:
    #             j = next[j]
    #         if s[i] == s[j+1]:
    #             j += 1
    #         next[i] = j

# @lc code=end

