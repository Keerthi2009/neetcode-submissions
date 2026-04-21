class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            substr=strs[0]
            for i in range(1,len(strs)):
                j=0
                while j<min(len(substr),len(strs[i])):
                    if substr[j] !=strs[i][j]:
                        break
                    j+=1
                substr=substr[:j]
            return(substr)        