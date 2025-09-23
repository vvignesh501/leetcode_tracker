class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # Create a hashMap with lastIndex
        partition = {}
        for i, c in enumerate(s):
            partition[c] = i

        size = 0
        end = 0
        res = []
        # When index 
        for i, c in enumerate(s):
            size += 1
            end = max(end, partition[c])

            if i == end:
                res.append(size)
                size = 0
        
        return res

# Time: O(n) → one pass to build last index, one pass to partition

# Space: O(1) → 26 chars at most
        