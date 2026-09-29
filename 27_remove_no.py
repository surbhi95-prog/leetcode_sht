class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for n in nums:
            if n!=val:
                nums[k]=n
                k=k+1
        return k,nums[:k]
                

        
obj = Solution()
print(obj.removeElement([3,2,2,3],3))
# print(obj.removeElement([0,1,2,2,3,0,4,2],2))