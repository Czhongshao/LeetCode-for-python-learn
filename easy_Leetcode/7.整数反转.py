#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # 转化成字符型，并计算长度
        num = str(x)
        # 建立空的字符串用于存储反转数
        num1 = ''
        n = len(num)
        if n == 1 or (n == 2 and x<0) :
            return x
        else:
            if x > 0:
                for i in range(n):
                    num1 += num[n-1-i]
            else:
                num1 += num[0]
                for i in range(1,n):
                        num1 += num[n-i]
            num1 = int(num1)
        if num1 > 2 ** 31 -1 or num1 < - 2 ** 31:
            return 0
        return num1
# @lc code=end

