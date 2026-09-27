class Solution(object):
    def sortArrayByParityII(self, nums):
        l=[]
        a=[]
        b=[]
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        for i in range(len(a)):
            l.append(a[i])
            l.append(b[i])            
        
        return l            


        
        