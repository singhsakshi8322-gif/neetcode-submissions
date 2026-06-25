class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=0
        for i in s:
            if i != ' ':
                r+=1
            elif r > 0:
                temp = r
                r = 0
        return r if r > 0 else temp