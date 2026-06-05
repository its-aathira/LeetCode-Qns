class Solution(object):
    def reverseVowels(self, s):
        vowels="aeiouAEIOU"
        vowel_list=[]
        for ch in s:
            if ch in vowels:
                vowel_list.append(ch)
        
        vowel_list.reverse()
        result=list(s)

        j=0
        for i in range(len(result)):
            if result[i] in vowels:
                result[i]=vowel_list[j]
                j+=1

        return "".join(result)
        