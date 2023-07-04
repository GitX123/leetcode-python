'''
No. 57
Medium
'''

from typing import List

class Solution(object):
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []

        for i in range(len(intervals)):
            # non-overlapping 
            if newInterval[1] < intervals[i][0]: # left-hand 
                newIntervals.append(newInterval)
                return newIntervals + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # right-hand
                newIntervals.append(intervals[i])
            # overlapping
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        newIntervals.append(newInterval) # rightmost case
        return newIntervals