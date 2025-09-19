/*
 * @lc app=leetcode.cn id=704 lang=c
 *
 * [704] 二分查找
 */

// @lc code=start
int search(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1; // 定义target在左闭右闭的区间里，[left, right]
    while(left <= right) { // 对于left=right, [left, right]依然成立
        int middle = left + ((right - left) / 2); // 防止溢出 其效果与 (left+right)/2 相同
        if (nums[middle] > target) {
            right = middle - 1; // target 在左区间，所以 [left, middle - 1]
        } else if (nums[middle] < target) {
            left = middle + 1; // target 在右区间，所以 [middle + 1, right]
        } else { // nums[middle] == target
            return middle; // 数组中找到目标值，直接返回下标
        }
    }
    // 未找到目标值
    return -1;
}
// @lc code=end

