#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## 同样的字母，通过组合形成不同的单词


        # 方法1：以数组作为哈希表，暴力求解，通过ASCII码得到某元素
        # # 新建26长空数组
        # record = [0] * 26

        # # 记录当前字母的数量
        # # ord转化成 ASCII码，只需要求出一个相对数值
        # for i in s:
        #     record[ord(i) - ord("a")] += 1
        
        # # 如果在下一个单词当中还有这个字母，那么就减去一位数
        # for i in t:
        #     record[ord(i) - ord("a")] -= 1

        # for i in range(26):
        #     if record[i] != 0:
        #         # 如果 record 数组当中有元素不为0，那么s和t绝对不是匹配的
        #         return False
        # return True


        # 方法2：非数组的哈希表，defaultdict 解题思路
        # from collections import defaultdict
        # # defaultdict 函数，强转字母成 int
        # s_dict = defaultdict(int)
        # t_dict = defaultdict(int)
        # for x in s:
        #     s_dict[x] += 1
        # for x in t:
        #     t_dict[x] += 1
        # return s_dict == t_dict


        # 方法3：非数组的哈希表，Counter
        from collections import Counter
        # 用于计算hash 的对象
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count

# @lc code=end

