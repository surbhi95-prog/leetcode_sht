class Solution(object):
    def isAnagram(self, s, t):
        i = len(s)-1
        if(len(s)!=len(t)):
            return False
        newstring= ""
        for c in s:
            if c in t:
                newstring = newstring+c
                t = t.replace(c,"",1)
            else:
                return False
        return len(newstring) == len(s)

# chars and their frequencies matter too
obj = Solution()
print(obj.isAnagram("arc", "car"))