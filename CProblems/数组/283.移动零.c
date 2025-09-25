/*
 * @lc app=leetcode.cn id=283 lang=c
 *
 * [283] 移动零
 */

// @lc code=start
void moveZeroes(int* nums, int numsSize) {
    // 双指针
    int i0 = 0;
    for (int i=0; i<numsSize; i++) {
        if (nums[i]) {
            int t=nums[i];
            nums[i]=nums[i0];
            nums[i0]=t;
            i0++;
        }
    }
}
// @lc code=end

