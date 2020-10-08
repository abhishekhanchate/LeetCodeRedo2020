# Day 4 
# Remove Covered Intervals

#Given a list of intervals, remove all intervals that are covered by another interval in the list.

#Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

#After doing so, return the number of remaining intervals.

#Example 1:
#Input: intervals = [[1,4],[3,6],[2,8]]
#Output: 2
#Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.


#Example 2:
#Input: intervals = [[1,4],[2,3]]
#Output: 1


#Example 3:
#Input: intervals = [[0,10],[5,12]]
#Output: 2


#Example 4:
#Input: intervals = [[3,10],[4,10],[5,11]]
#Output: 2


#Example 5:
#Input: intervals = [[1,2],[1,4],[3,4]]
#Output: 1


#Constraints:
#1 <= intervals.length <= 1000
#intervals[i].length == 2
#0 <= intervals[i][0] < intervals[i][1] <= 10^5
#All the intervals are unique.

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #               [[1,2],[1,4],[3,4]]             Output = 2    Expected = 1    
        intervals.sort()
        c, d = intervals[0]
        count = 0
        i = 1
        
        while i < len(intervals):
            
            a, b = intervals[i]
            
            if c == a and d <= b:
                count += 1
            
            if c <= a and b <= d:
                count += 1
                i += 1
            
            else:
                c, d = intervals[i]
                i += 1
        
        return len(intervals) - count   

# Brute Force        
#        remain = len(intervals)
#        for i, (a, b) in enumerate(intervals):
#            for j, (c, d) in enumerate(intervals):
#                if i != j and c <= a and b <= d:
#                    remain -= 1
#                    break
#        return remain

    
    
    
#        count = 0        
#        for i in range(len(intervals)):
       
#            for j in range(len(intervals)):
            
#                ind = intervals[i]
#                indd = intervals[j]
                
#                if ind == indd:
#                    continue
                    
#                a = ind[0]
#                print(a)
#                b = ind[1]
#                print(b)                                    

#                c = indd[0]
#                print(c)
#                d = indd[1]
#                print(d)

#                if c <= a and b <= d:
#                    count = count + 1
        
#        print(len(intervals))
#        print(count)
        
#        return(len(intervals) - count)


    
    