class Solution(object):
    def isPalindrome(self, s):
        # print(s.replace(" ",""))
        n=""
        for ch in s.lower():
            if ch.isalnum():
                n=n+ch
        return n==n[::-1]

obj = Solution()
print(obj.isPalindrome("0P"))     