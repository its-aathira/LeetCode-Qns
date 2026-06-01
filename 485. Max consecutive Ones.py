class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        big=0
        for num in nums:
            if num==1:
                count+=1
                big = max(big,count)
            else:
                count=0
        return big
        