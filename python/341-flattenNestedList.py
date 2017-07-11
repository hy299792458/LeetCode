# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        store = nestedList
        while any(type(node) != int for node in store):
            temp = []
            for node in store:
                if type(node) == int:
                    temp.append(node)
                elif type(node) == list:
                    temp += node
                elif node.isInteger():
                    temp.append(node.getInteger())
                else:
                    temp += node.getList()
            store = temp
        self.store = store
        self.p = 0
        self.length = len(store)

    def next(self):
        self.p += 1
        return self.store[self.p - 1]
        

    def hasNext(self):
        return self.p < self.length

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
