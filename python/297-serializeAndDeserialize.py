# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        level = [root]
        res = []
        while level:
            newLevel = []
            for node in level:
                if node:
                    res.append(node.val)
                    newLevel.append(node.left)
                    newLevel.append(node.right)
                else:
                    res.append(None)
            level = newLevel
        return ",".join(map(str, res))
        

    def deserialize(self, data):
        nodes = data.split(",")
        root = TreeNode(int(nodes[0])) if nodes[0] != 'None' else None
        level = [root]
        pos = 0
        newLevel = []
        for node in nodes[1:]:
            if node != 'None':
                if pos % 2 == 0:
                    level[pos / 2].left = TreeNode(int(node))
                    newLevel.append(level[pos / 2].left)
                else:
                    level[pos / 2].right = TreeNode(int(node))
                    newLevel.append(level[pos / 2].right)
            pos += 1
            if pos == len(level) * 2:
                level = newLevel
                newLevel = []
                pos = 0
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
