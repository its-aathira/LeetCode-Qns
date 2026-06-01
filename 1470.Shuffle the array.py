class Solution(object):
    def shuffle(self, nums, n):
        sol=[]
        for i in range(n):
            sol.append(nums[i])
            sol.append(nums[i+n])
        return sol