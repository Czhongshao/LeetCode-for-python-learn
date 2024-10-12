#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 方法1
        # # 如果为负数，就不是回文数
        # if x < 0:
        #     return False
        # # 记录长度
        # x = str(x)
        # n = len(x)
        # for i in range(n):
        #     # 只要有一个不满足回文条件，就返回错误
        #     if x[i] != x[n-1-i]:
        #         return False
        # return True

        # 方法2
        # 负数不是回文数
        # if x < 0:
        #     return False
        # y = int(str(x)[::-1])
        # return x == y
     
        # 方法3
        # 负数和个位是0的不是回文数
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        # 判断偶数长度是否相等，奇数长度需要排除掉中间那个数
        return x == y or x == y // 10
# @lc code=end

