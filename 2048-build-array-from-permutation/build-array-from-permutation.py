class Solution(object):
    def buildArray(self, nums):
        
        ans=[]
        n=len(nums)
        for i in range(0,n):
            ans.append(nums[nums[i]])
        return ans    
                    

        
        