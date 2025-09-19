#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 解法1
        # # 统计元素出现频率
        # map_ = {} # nums[i]：对应出现的次数
        # for i in range(len(nums)):
        #     map_[nums[i]] = map_.get(nums[i], 0) + 1

        # # 对频率排序
        # # 定义一个小顶堆，大小为k
        # pri_que = [] # 小顶堆

        # # 用固定大小为k的小顶堆，扫描所有频率的数值
        # for key, freq in map_.items():
        #     heapq.heappush(pri_que, (freq, key))   
        #     if len(pri_que) > k: # 如果堆的大小大于k，队列弹出，保证堆的大小一直为k
        #         heapq.heappop(pri_que)

        # # 找出前k个高频元素，因为小顶堆会优先弹出最小的，所以倒序输出到数组
        # result = [0] * k
        # for i in range(k-1, -1, -1):
        #     result[i] = heapq.heappop(pri_que)[i]
        # return result

        # 解法2
                # 使用字典统计数字出现次数
        time_dict = defaultdict(int)
        for num in nums:
            time_dict[num] += 1
        # 更改字典，key为出现次数，value为相应的数字的集合
        index_dict = defaultdict(list)
        for key in time_dict:
            index_dict[time_dict[key]].append(key)
        # 排序
        key = list(index_dict.keys())
        key.sort()
        result = []
        cnt = 0
        # 获取前k项
        while key and cnt != k:
            result += index_dict[key[-1]]
            cnt += len(index_dict[key[-1]])
            key.pop()

        return result[0: k]
        
# @lc code=end

