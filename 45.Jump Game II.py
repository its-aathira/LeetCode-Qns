class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        jumps,farthest,current_end=0,0,0
        for i in range(len(nums)-1):
            farthest = max(farthest,i+nums[i])
            if i == current_end:
                jumps+=1
                current_end=farthest
            if current_end > len(nums)-1:
                break 
        return jumps
        