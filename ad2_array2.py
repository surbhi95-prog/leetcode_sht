# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         i=0
#         while i!= len(digits)-1:
#             i=i+1
#         if digits[i] < 9:
#             digits[i]= digits[i]+1
#             # digits[i+1]=0
#         else:
#             digits[i]=digits[i]+1
#         return digits
#         # return digits
        

# obj = Solution()
# print(obj.plusOne([9,9]))

class Solution(object):
    def plusOne(self, digits):

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        digits.insert(0, 1)
        return digits
    
obj = Solution()
print(obj.plusOne([9,9,9,9]))