#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:


        # 方法1：集合
    #     record = set()
    #     while True:
    #         n = self.get_sum(n)
    #         if n == 1:
    #             return True
            
    #         # 如果中间结果出现重复，那么就是进入了死循环，不是快乐数
    #         if n in record:
    #             return False
    #         else:
    #             record.add(n)
    # # 平方求和函数
    # def get_sum(self,n:int) -> int:
    #     new_num = 0
    #     while n:
    #         n, r = divmod(n, 10)
    #         new_num += r ** 2
    #     return new_num
    

        # 方法2：集合
        # record = set()
        # while n not in record:
        #     record.add(n)
        #     new_num = 0 
        #     n_str = str(n)
        #     for i in n_str:
        #         new_num += int(i) ** 2
        #     if new_num == 1:
        #         return True
        #     else:
        #         n = new_num
        # return False
    

        # 方法3：数组
        record = []
        while n not in record:
            record.append(n)
            new_num = 0
            n_str = str(n)
            for i in n_str:
                new_num += int(i) ** 2
            if new_num == 1:
                return True
            else:
                n = new_num
        return False



# @lc code=end

