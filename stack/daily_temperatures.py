from typing import List

'''
No. 739

Elements we need:
* A monotonic decreasing stack

1. Push temperatures and indices into stack.
2. If the recently pushed temperature is bigger thant the previous one,
pop until it is smaller than the previous one.

'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            pass

        return result