#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Python 普通的 Queue 或 SimpleQueue 没有类似于 peek 的功能
        也无法用索引访问, 在实现 top 的时候较为困难。

        用 list 可以，但是在使用 pop(0) 的时候时间复杂度为O(n)
        因此这里可以使用双向队列，我们保证只执行 popleft() 和 append(), 因为 deque 可以用索引访问, 可以实现和 peek 相似的功能

        in - 存所有数据
        out - 仅在 pop 的时候会用到
        """
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        """
        直接 append 即可
        """
        self.queue_in.append(x)
    
    def pop(self) -> int:
        """
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个
        
        tip：这不能像栈实现队列一样，因为另一个queue也是FIFO，如果执行pop()它不能像
        stack一样从另一个pop()，所以干脆in只用来存数据，pop()的时候两个进行交换
        """
        if self.empty():
            return None

        for _ in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft()) 

        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()       

    def top(self) -> int:
        """
        写法一：
        1. 首先确认不空
        2. 我们仅有in会存放数据，所以返回第一个即可（这里实际上用到了栈）
        写法二：
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个，并使用temp变量暂存
        6. 把temp追加到queue_in的末尾
        """
        # 写法1:
        # if self.empty():
        #     return None
        # return self.queue_in[-1] # 这里实际上用到了栈，因为直接获取了queue_in的末尾元素

        # 写法2:
        if self.empty():
            return None
        
        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        temp = self.queue_out.popleft()
        self.queue_in.append(temp)
        return temp

    def empty(self) -> bool:
        """
        因为只有 in 存了数据, 只要判断 in 是不是有数即可
        """
        return len(self.queue_in) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

