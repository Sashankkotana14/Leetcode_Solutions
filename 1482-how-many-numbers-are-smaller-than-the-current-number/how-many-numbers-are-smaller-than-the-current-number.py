class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count=0
        l=[]
        for i in range(0,len(nums)):
            count=0
            for j in range(0,len(nums)):
                if  nums[j]<nums[i]:
                    count+=1
            l.append(count)
        return l    


        