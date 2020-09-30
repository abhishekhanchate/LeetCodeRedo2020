#1281. Subtract the Product and Sum of Digits of an Integer

# While and using Remainder 28 ms, Faster than 77.69%, 14.1 MB, Less than 5.01%
#class Solution:
#    def subtractProductAndSum(self, n: int) -> int:
        
#        prod = 1
#        summ = 0

#        while n > 0:
#            prod *= n % 10
#            summ += n % 10
#            n = n//10
        
#        return prod - summ


# For and using String 24 ms, Faster than 93.55%, 14.1 MB, Less than 5.58%
class Solution:    
    def subtractProductAndSum(self, n: int) -> int:
        
        nums = list(str(n))
        prod = 1
        summ = 0
        
        for num in nums:
            numm = int(num)
            prod *= numm
            summ += numm
            
        return prod - summ