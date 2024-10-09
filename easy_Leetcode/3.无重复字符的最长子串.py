#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 初始化遍历长度
        n = len(s)
        # 初始化字典存储字符串
        a = {}
        # 初始化最大字符串数
        maxlenth = 0
        # 初始化j
        j = 0
        
        # # 如果输入的字串为一个，那么这个就是最长字串
        # for i in range(n):
        #     # 如果该字符在字典当中没有找到，那么就执行存储步骤
        #     if s[i] not in a:
        #         # 添加进入字典当中
        #         # 当i=0,j=0,max=0时，仍然需要存储一个字符
        #         maxlenth = max(maxlenth,i-j+1)
        #     else:
        #         # 更新j为当前字符上次出现的位置的下一个位置
        #         j = max(j, a[s[i]]+1)
        #     # 字典键值对
        #     a[s[i]] = i
        # return maxlenth

        # 如果输入的字串为一个，那么这个就是最长字串
        for i in range(n):
            # 如果该字符在字典当中没有找到，那么就执行存储步骤
            if s[i] in a:
                j = max(j, a[s[i]]+1)
            if i - j +1 >=maxlenth:
                maxlenth = max(maxlenth,i-j+1) 
            a[s[i]] = i
        return maxlenth
# @lc code=end