# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        nodes = {}
        def build(node):
            if node.label not in nodes:
                nodes[node.label] = UndirectedGraphNode(node.label)
                for nb in node.neighbors:
                    nodes[node.label].neighbors.append(build(nb))
            return nodes[node.label]
        if node:
            return build(node)        
