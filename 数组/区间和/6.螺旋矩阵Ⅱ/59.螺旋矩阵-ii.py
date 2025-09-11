#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 创建一个n*n的矩阵
        # 全部用0进行填充
        luoxuan = [[0] * n for _ in range(n)] 
        
        # 起始点
        startx, starty = 0,0
        # 迭代次数，n为奇数，矩阵的中心点
        loop, mid = n // 2, n // 2
        # 计数
        count = 1

        # 每循环一层偏移量+1，偏移量从1开始
        for offset in range(1, loop + 1):
            # 从左至右，左闭右开
            for i in range(starty, n - offset):
                luoxuan[startx][i] = count
                count += 1
            # 从上至下，左闭右开
            for i in range(startx, n - offset):
                luoxuan[i][n - offset] = count
                count += 1
            # 从右至左，左闭右开
            for i in range(n - offset, starty, -1):
                luoxuan[n - offset][i] = count
                count += 1
            # 从下至上，左闭右开
            for i in range(n - offset, startx, -1):
                luoxuan[i][starty] = count
                count += 1
            # 更新起始点
            startx += 1
            starty += 1

        if n % 2 != 0:
            luoxuan[mid][mid] = count
        return luoxuan
# @lc code=end

