/*
 * @lc app=leetcode.cn id=844 lang=c
 *
 * [844] 比较含退格的字符串
 */

// @lc code=start
char* build(char* str) {
    int n = strlen(str), len = 0;
    char* ret = malloc(sizeof(char) * (n + 1));
    for (int i = 0; i < n; i++) {
        if (str[i] != '#') {
            ret[len++] = str[i];
        } else if (len > 0) {
            len --;
        }
    } 
    ret[len] = '\0';
    return ret;
}
bool backspaceCompare(char* s, char* t) {
    return strcmp(build(s), build(t)) == 0;
}
// @lc code=end

