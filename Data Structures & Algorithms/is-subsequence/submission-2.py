class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        #j=0
        for a in t:
            if i < len(s) and a == s[i] :
                i=i+1
        return i ==len(s)   