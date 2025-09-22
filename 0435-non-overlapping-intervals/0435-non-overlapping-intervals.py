class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Trick - sort the intervals, compare the prev with the current list
        # Skip if overlapping, overlapping = last value in prev = first value in curr
        
        intervals.sort()
        res = 0

        # Get the first row last col values as prev
        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if prev <= start:
                prev = end
            else:
                res += 1
                prev = min(prev, end)
        return res

  # Time - O(nlogn)
  # Space - O(1)      

        