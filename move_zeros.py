def moveZerosToEnd(nums):
    i = 0
    for num in nums:
        if num!=0:
            nums[i]=num
            i=i+1
    while i<len(nums):
        nums[i]=0
        i=i+1
    return nums

print(moveZerosToEnd([0,1,0,3,12,0,0,17]))
# o/p [1,3,12,0,0]

# def moveZerosToFront(nums):
#     i = len(nums)-1
#     for num in
#     return nums

# print(moveZerosToFront([0,1,0,3,12,0,0,17]))