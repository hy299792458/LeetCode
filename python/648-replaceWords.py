class Solution(object):
    def replaceWords(self, dict, sentence):
        dict = set(dict)
        def replace(word):
            for i in range(1, len(word)):
                if word[: i] in dict:
                    return word[: i]
            return word
        words = sentence.split(" ");
        return " ".join(map(replace, words))
