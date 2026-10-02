class Solution(object):
    def plusOne(self,digits):
        i=len(digits)-1
        while i>=0:
            if digits[i]==9:
                digits[i]=0 # change every 9 to 0, and move to the next digit
                i=i-1
            else: 
                digits[i]=digits[i]+1
                return digits # if change is made to only last digit, return it right away
        digits.insert(0,1)
        return digits