class Solution(object):
    def fullJustify(self, words, maxWidth):
        group = []
        l = []
        length = 0
        for word in words:
            if not l:
                l.append(word)
                length += len(word)
            else:
                if length + 1 + len(word) <= maxWidth:
                    l.append(word)
                    length += 1 + len(word)
                else:
                    group.append(l[:])
                    l = [word]
                    length = len(word)
        if l:
            group.append(l)
        
        def just(line):
            spaces = maxWidth - sum(len(word) for word in line)
            count = len(line) - 1
            try:
                space = spaces / count
                left = spaces % count
                res = [line[0]]
                for word in line[1:]:
                    if left:
                        left -= 1
                        res += [' ' * (space + 1), word]
                    else:
                        res += [' ' * (space), word]
            except:
                res = [line[0], ' ' * spaces]
            return ''.join(res)
        last = ' '.join(group[-1])
        last = last + ' ' * (maxWidth - len(last))
        return map(just, group[:-1]) + [last]
