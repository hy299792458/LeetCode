class Solution(object):
    def detectCapitalUse(self, word):
        if word.lower() == word:
            return True
        if word[0] == word[0].upper():
            if word[1:].lower() == word[1:]:
                return True
            if word[1:].upper() == word[1:]:
                return True
        return False
