class Solution(object):
    def findTheDifference(self, s, t):
        for ch in s:
            if ch in t:
                t=t.replace(ch,"",1)
            
        return t
        