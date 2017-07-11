class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.s = -1
        self.e = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        try:
            self.q[self.e] = x
        except:
            self.q.append(x)
        self.e += 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.s += 1
        return self.q[self.s]
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.q[self.s + 1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.s + 1 == self.e
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
