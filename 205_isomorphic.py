class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) !=  len(t)):
            return False
        freqS = {}
        for ch in s:
            freqS[ch] = freqS.get(ch,0) + 1

        freqT = {}
        for ch in t:
            freqT[ch] = freqT.get(ch,0) + 1
        
        return sorted(list(freqS.values())) == sorted(list(freqT.values()))
        # return list(freqS.values()) == list(freqT.values())
        