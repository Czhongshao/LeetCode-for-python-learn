/*
 * @lc app=leetcode.cn id=26 lang=c
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
int removeDuplicates(int* nums, int numsSize) {
    // 双指针
    int slowIndex=0;
    for (int fastIndex=0; fastIndex<numsSize; fastIndex++) {
        if (nums[slowIndex] != nums[fastIndex]) {
            slowIndex++;
            nums[slowIndex] = nums[fastIndex];
        }
    }
    return slowIndex+1;
}
// @lc code=end

