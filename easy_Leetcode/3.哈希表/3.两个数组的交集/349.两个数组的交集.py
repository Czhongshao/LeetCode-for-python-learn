#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # # 方法1：暴毙了
        # ss = []
        # k = 0

        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             ss += [nums1[i]]
        #             k += 1

        # return ss

        # # 方法2：集合+字典
        # # 使用哈希表存储一个数组中的全部元素
        # table = {}
        # for num in nums1:
        #     table[num] = table.get(num, 0) + 1
        
        # # 使用集合存储结果
        # res = set()
        # for num in nums2:
        #     if num in table:
        #         res.add(num)
        #         del table[num]
        # return list(res)
    
        
        # # 方法3：数组解法？？
        # count1 = [0] * 1001
        # count2 = [0] * 1001
        # result = []

        # for i in range(len(nums1)):
        #     count1[nums1[i]] += 1
        # for j in range(len(nums2)):
        #     count2[nums2[j]] += 1
        # for k in range(1001):
        #     if count1[k] * count2[k] > 0:
        #         result.append(k)
        # return result


        # 方法4：集合一行？？
        return list(set(nums1) & set(nums2))
            

# @lc code=end

