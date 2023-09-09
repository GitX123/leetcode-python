'''
No. 56
Medium
'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals according to the first element start_i of each interval
        intervals.sort(key=lambda i : i[0])

        new_intervlas = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = new_intervlas[-1][1]

            if start <= lastEnd:
                new_intervlas[-1][1] = max(lastEnd, end)
            else:
                new_intervlas.append([start, end])
        
        return new_intervlas