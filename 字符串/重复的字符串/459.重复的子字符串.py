#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ...
        # 方法1:前缀表减一
        # if len(s) == 0:
        #     return False
        # nxt = [0] * len(s)
        # self.getNext(nxt, s)
        # if nxt[-1] != -1 and len(s) % (len(s) - (nxt[-1] + 1)) == 0:
        #     return True
        # return False
    
    # 方法1:前缀表减一
    # def getNext(self, nxt, s):
    #     nxt[0] = -1
    #     j = -1
    #     for i in range(1, len(s)):
    #         while j >= 0 and s[i] != s[j+1]:
    #             j = nxt[j]
    #         if s[i] == s[j+1]:
    #             j += 1
    #         nxt[i] = j
    #     return nxt
    

        # 方法2:find
        # n = len(s)
        # if n <= 1:
        #     return False
        # ss = s[1:] + s[:-1]
        # print(ss.find(s))
        # return ss.find(s) != -1

        # 方法3:暴力
        n = len(s)
        if n <= 1:
            return False
        
        substr = ""
        for i in range(1, n//2 + 1):
            if n % i == 0:
                substr = s[:i]
                if substr * (n//i) == s:
                    return True
        return False

# @lc code=end

