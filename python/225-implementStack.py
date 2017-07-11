class MyStack(object):

    def __init__(self):
        self.q = []
        

    def push(self, x):
        self.q.append(x)

    def pop(self):
        self.q, res = self.q[0:-1], self.q[-1]
        return res
        
    def top(self):
        self.q, res = self.q[0:-1], self.q[-1]
        self.q.append(res)
        return res

    def empty(self):
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
