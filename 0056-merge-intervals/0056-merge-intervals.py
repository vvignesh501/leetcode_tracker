class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda i:i[0])
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastStart, lastEnd = output[-1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output

# Time - O(nlogn) - sorting
# Space - O(n)