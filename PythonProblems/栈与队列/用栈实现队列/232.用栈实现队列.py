#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        in 主要负责 push, out 主要负责 pop
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        有新元素进来, 就往 in 里面 push
        """
        self.stack_in.append(x)
        
    def pop(self) -> int:
        """
        从队列前删除元素并返回该元素
        """
        if self.empty():
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        
    def peek(self) -> int:
        """
        获得前端元件
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans        

    def empty(self) -> bool:
        """
        只要 in 或者 out 有元素, 说明队列不为空
        """
        return not (self.stack_in or self.stack_out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

