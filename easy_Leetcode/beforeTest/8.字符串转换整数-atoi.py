#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # # 记录字符串的长度
        # n = len(s)
        # if n == 0:
        #     return 0
        
        # # 确定数字出现的位置
        # i = 0
        # while i < n and s[i] == ' ':
        #     i += 1
        # # 判断符号
        # fuhao = 1
        # if i < n and (s[i] == '-' or s[i] == '+'):
        #     # 如果是-就左边，反之右边
        #     fuhao = -1 if s[i] == '-' else 1
        #     i += 1

        # # num1 = 0
        # ##
        # num1 = ''
        # ##
        # for j in range(i,n):
        #     # 如果不是数字的话，就跳过不进行存储
        #     if s[j] < '0' or s[j] > '9':
        #         break
        #     # num1 = num1 * 10 + ord(s[j]) - ord('0')
        # ##
        #     num1 += s[j]
        # if num1 == '':
        #     return 0
        # ##
        # num1 = int(num1)
        # if fuhao == 1 and num1 > 2 ** 31 - 1:
        #     return 2 ** 31 - 1
        # if fuhao == -1 and -num1 < -2 ** 31:
        #     return -2 ** 31
        # return num1 * fuhao
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 -1), -2**31)
# @lc code=end

