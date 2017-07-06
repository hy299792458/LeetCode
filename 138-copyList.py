# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        orig = []
        while head:
            orig.append(head)
            head = head.next
        newList = [RandomListNode(node.label) for node in orig]
        for i in range(len(newList) - 1):
            newList[i].next = newList[i + 1]
        for a, b in zip(newList, orig):
            if b.random == None:
                a.random = None
            else:
                a.random = newList[orig.index(b.random)]
        return newList[0]
