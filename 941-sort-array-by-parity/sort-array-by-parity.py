class Solution(object):
    def sortArrayByParity(self, nums):
        l=[]
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                l.append(nums[i])
        for j in range(0,len(nums)):
            if nums[j]%2!=0:
                l.append(nums[j])  
        return l              
        