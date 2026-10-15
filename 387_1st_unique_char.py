class Solution(object):
    def firstUniqChar(self,s):

        freq = {} # dict for ch -> freq mapaping
        repeated = set() # set for storing unique chars onlyyy

        for ch in s:
            freq[ch] = freq.get(ch,0)+1 # if freq is 0, add 1 to it
            if freq[ch] >1:
                repeated.add(ch)

        for i,ch in enumerate(s): # enumerate cz we want to return index
            if ch not in repeated:
                return i
        return -1