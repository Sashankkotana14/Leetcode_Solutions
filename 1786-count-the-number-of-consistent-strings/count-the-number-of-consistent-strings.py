class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for i in range(0, len(words)):
            for j in range(0, len(words[i])):
                if words[i][j] not in allowed:
                    break
            else:
                count += 1

        return count         

                  
        