/*
 * @lc app=leetcode.cn id=27 lang=c
 *
 * [27] 移除元素
 */

// @lc code=start
int removeElement(int* nums, int numsSize, int val) {
    // 暴力解
    // for (int i=0; i<numsSize; i++) {
    //     if (nums[i] == val) {
    //         for (int j=i+1; j<numsSize; j++) {
    //             nums[j-1] = nums[j];
    //         }
    //         i--;
    //         numsSize--;
    //     }
    // }
    // return numsSize;

    // 双指针
    int slowIndex = 0;
    for (int fastIndex=0; fastIndex<numsSize; fastIndex++) {
        if (val!= nums[fastIndex]) {
            nums[slowIndex++] = nums[fastIndex];
        }
    }
    return slowIndex;
}
// @lc code=end

