class Solution(object):
    def runningSum(self, nums):
        running_Sum=[]
        currentSum=0
        for i in  nums:
            currentSum+=i
            running_Sum.append(currentSum)
        return running_Sum