#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # 如果行数为 1，直接返回原字符串，因为不需要变换
        if numRows <= 1:
            return s
        # 方法1
        # else:
        #     # 计算每个 Z 字形的步长
        #     # 步长范围是某个元素到下一列同行的举例
        #     step = 2 * numRows - 2
        #     # 首先，将字符串按照步长进行分组，得到每行的第一个字符
        #     r = s[::step]
        #     # 遍历每一行（除了第一行和最后一行）
        #     for i in range(1, numRows - 1):
        #         # 从第 i 个字符开始，每隔 step 个字符取一个字符，直到字符串结束
        #         a = s[i :: step]
        #         # 从倒数第 i 个字符开始，每隔 step 个字符取一个字符，直到字符串结束
        #         b = s[step - i :: step]

        #         # 将 a 和 b 交错合并，因为 a 和 b 的长度可能不同
        #         min_len = min(len(a), len(b))
        #         # 创建一个长度为 min_len * 2 的列表，用于存储交错合并的结果
        #         res = [''] * min_len * 2
        #         # 将 a 的字符放入列表的偶数位置
        #         res[::2] = a[:min_len]
        #         # 将 b 的字符放入列表的奇数位置
        #         res[1::2] = b[:min_len]
        #         # 将列表转换为字符串，并与 a 和 b 的剩余部分合并
        #         r += ''.join(res) + a[min_len:] + b[min_len:]
        #     # 将所有行合并，并返回最终的字符串
        #     return r + s[numRows - 1::step]
        
        # 方法2
        # 初始化一个空列表，长度为行数，每个元素均是空字符串
        list_1 = ['' for _ in range(numRows)]
        # down控制行数增减，down = 1代表行数增加；反之，行数减少
        down = -1
        # 记录此时的行数
        row = 0
        for ch in s:
            # 存入此行的字符
            list_1[row] += ch
            # 如果此时是最后一行或者第一行，那么就更换方向
            if row == numRows - 1 or row == 0:
                down *= -1
            # 更换行数
            row += down
        # 将列表当中的字符串相连接，并返回此值
        return ''.join(list_1)

# @lc code=end