class Solution(object):
    def countQuadruplets(self, nums):
        count=0
        for a in range(0,len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(b+1,len(nums)):
                    for d in range(c+1,len(nums)):
                        if nums[a]+nums[b]+nums[c]==nums[d]:
                            count+=1
        return count                    
        
        