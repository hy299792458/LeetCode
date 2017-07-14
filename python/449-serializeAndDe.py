# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        level = [root]
        while level:
            newLevel = []
            temp = []
            for node in level:
                if node:
                    newLevel.append(node.left)
                    newLevel.append(node.right)
                    temp.append(str(node.val))
                else:
                    temp.append('.')
            level = newLevel
            res.append(','.join(temp))
        #print res
        return ';'.join(res)
        

    def deserialize(self, data):
        levels = map(lambda x: x.split(','), data.split(';'))
        if not levels or levels[0][0] == '.':
            return None
        head = TreeNode(int(levels[0][0]))
        build = [head]
        for l in levels[1:]:
            newBuild = []
            for i in range(len(l)):
                if l[i] != '.':
                    if i % 2 == 0:
                        build[i / 2].left = TreeNode(int(l[i]))
                        newBuild.append(build[i / 2].left)
                    else:
                        build[i / 2].right = TreeNode(int(l[i]))
                        newBuild.append(build[i / 2].right)
            build = newBuild
        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
