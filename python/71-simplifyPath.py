class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        last = ''
        for node in path.split('/'):
            if node == '.' or node == '':
                continue
            elif node == '..':
                stack = stack[:-1]
            else:
                stack.append(node)
            last = node
        return '/' + '/'.join(stack)
