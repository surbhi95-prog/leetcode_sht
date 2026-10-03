class Solution(object):
    def lengthOfLastWord(self, s):
        list1 = s.split()
        n = len(list1)-1
        return len(list1[n])

# obj = Solution()
# print(obj.lengthOfLastWord("     fly  me      to the      moon     "))

# submit this