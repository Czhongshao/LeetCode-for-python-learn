#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 如果s的数量少于t，那么必定不符合
        if len(s) < len(t):
            return ""
        
        # 初始化结果
        ans = float("inf"), None

        # 统计t中每个字符出现的次数
        t_count = Counter(t)
        required = len(t_count) # 需要包含不同的字符数

        # 用于记录当前窗口中字符的出现次数
        window_counts = Counter()
        # 初始化左右指针
        left, right = 0, 0
        
        # 初始化满足条件的字符数
        formed = 0

        while right < len(s):
            # 将右指针的字符加入窗口
            window_counts[s[right]] += 1

            # 如果当前字符满足条件，则增加formed
            if s[right] in t_count and window_counts[s[right]] == t_count[s[right]]:
                formed += 1
            
            # 尝试缩小窗口直到不满足条件
            while left <= right and formed == required:
                char = s[left]

                # 检查是否需要更新结果
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left)

                # 将左指针的字符移除窗口
                window_counts[char] -= 1

                # 如果当前字符不满足条件，则减少formed
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                # 移动左指针
                left += 1
            # 移动右指针
            right += 1
        # 返回结果
        if ans[0] != float("inf"):
            return s[ans[1]:ans[1] + ans[0]]
        else:
            return ""
        
# @lc code=end

