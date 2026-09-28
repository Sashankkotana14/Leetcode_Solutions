class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum=0
        for i in range(0,len(s)):
            for j in range(0,len(t)):
                if s[i]==t[j]:

                    a= abs( i-(j))
                    sum+=a
                   
        return sum           
        