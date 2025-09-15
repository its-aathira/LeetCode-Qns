class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        count=0
        for i in text.split():
            for j in i:
                if j in brokenLetters:
                    break
            else:
                count+=1
        return count 
        