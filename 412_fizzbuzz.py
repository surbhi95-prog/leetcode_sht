class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ls=[]
        # i=1
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 ==0:
                ls.append("FizzBuzz")
            elif i % 5 == 0:
                ls.append("Buzz")
            elif (i % 3 == 0):
                ls.append("Fizz")
            else:
                ls.append(str(i))
        return ls

        return ls

            
        