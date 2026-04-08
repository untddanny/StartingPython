class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        first =strs[0]
        for i in range(len(first)):
            for words in strs[1:]:
                if (i==len(words) or first[i]!=words[i]):

                    return first[0:i]
        return first      
