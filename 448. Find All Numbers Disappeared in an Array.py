class Solution(object):
    def findDisappearedNumbers(self, nums):
        s=set(nums)
        missing=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                missing.append(i)
        return missing 
                