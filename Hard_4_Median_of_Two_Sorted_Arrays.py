# 4. Median of Two Sorted Arrays

# 96 ms, Faster than 70.32 %, 14.5 MB, Less than 5.17 %
#class Solution:
#    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#        summ = nums1 + nums2
#        sortedsumm = sorted(summ)
#        if len(sortedsumm)%2 != 0:
#            return sortedsumm[len(sortedsumm)//2]
#        else:
#            return (sortedsumm[len(sortedsumm)//2] + sortedsumm[(len(sortedsumm)//2)-1])/2
        
# 84 ms, Faster than 97.51 %, 14.4 MB, Less than 6.65%    
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length%2 == 0:
            return (nums1[length//2-1] + nums1[length//2])/2
        else:
            return nums1[length//2]