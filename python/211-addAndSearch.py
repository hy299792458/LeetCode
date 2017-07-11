class WordDictionary(object):
#using prefix tree
    def __init__(self):
        self.diction = [{}]

    def addWord(self, word):
        pos = 0
        for char in word:
            if char not in self.diction[pos]:
                self.diction[pos][char] = len(self.diction)
                self.diction.append({})
            pos = self.diction[pos][char]
        char = '$'
        if char not in self.diction[pos]:
            self.diction[pos][char] = len(self.diction)
            self.diction.append({})
        pos = self.diction[pos][char]

        
    def search(self, word):
        def match(word, i, pos):
            if i == len(word):
                if '$' in self.diction[pos]:
                    return True
                return False
            if word[i] == '.':
                return any(match(word, i + 1, self.diction[pos][k]) for k in self.diction[pos])
            elif word[i] in self.diction[pos]:
                return match(word, i + 1, self.diction[pos][word[i]])
            return False
        return match(word, 0, 0)


class WordDictionary(object):
#use length list
    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False
