#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # # s末尾指针
        # ps = len(s) - 1
        # # t末尾指针
        # pt = len(t) - 1

        # while ps >= 0 or pt >= 0:
        #     # 对s进行遍历
        #     while ps >= 0:
        #         if s[ps] == '#':
        #             ps -= 1
        #         else:
        #             break
        #     # 对t进行遍历
        #     while pt >= 0:
        #         if t[pt] == '#':
        #             pt -= 1
        #         else:
        #             break    
        #     if ps >= 0 and pt >= 0:
        #         if s[ps] != t[pt]:
        #             return False
        #         elif ps >= 0 or pt >= 0:
        #             return False
        #     ps -= 1
        #     pt -= 1

        # 方法1：按顺序存进新的字符串，如果识别到了#，那就删去整个字符串最后一个
        # 初始化两个空字符串ss和tt，用于存储处理退格操作后的s和t
        ss = ''
        tt = ''
        # 遍历字符串s
        for i in s:
            # 如果当前字符是'#'，并且ss不为空
            if i == '#':
                if ss:
                    # 删除ss的最后一个字符，模拟退格操作
                    ss = ss[:-1]
            else:
                # 如果当前字符不是'#'，则将其添加到ss的末尾
                ss += i
        # 遍历字符串t
        for j in t:
            if j == '#':
                if tt:
                    tt = tt[:-1]
            else:
                tt += j
        return ss == tt

        # # 方法2：双指针
        # sp = len(s) - 1
        # tp = len(t) - 1


# @lc code=end

