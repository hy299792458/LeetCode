class Solution(object):
    def findDuplicate(self, paths):
        files = collections.defaultdict(list)
        for path in paths:
            p_f = path.split(' ')
            p = p_f[0]
            for file in p_f[1:]:
                f_c = file.split('(')
                files[f_c[-1]].append(p + '/' + f_c[0])
        return [files[k] for k in files if len(files[k]) > 1]
