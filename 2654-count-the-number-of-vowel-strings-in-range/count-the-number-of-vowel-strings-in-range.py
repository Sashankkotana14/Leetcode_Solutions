class Solution(object):
    def vowelStrings(self, words, left, right):
        count=0
        for i in range(left,right+1):
            if words[i][0] in ('a','e','i','o','u') and words[i][-1] in ('a','e','i','o','u'):
                count+=1
        return count        

        
        