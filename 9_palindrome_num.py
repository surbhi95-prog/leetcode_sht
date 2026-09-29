class Solution(object):
    def isPalindrome(self, x):
        if x>=0:
            num_str = str(x)
            if(int(num_str[::-1]) == x):
                return True
            else:
                return False
        elif(x<0):
            pos_num = abs(x)
            num_str= str(pos_num)
            if(int(num_str[::-1]) == x):
                return True
            else:
                return False
        