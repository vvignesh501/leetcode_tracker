class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        max_a, max_b, max_c = 0, 0, 0

        for x, y, z in triplets:
            if x <= a and y <= b and z <= c:
                max_a, max_b, max_c = max(max_a, x), max(max_b, y), max(max_c, z)
        
        return [max_a, max_b, max_c] == target

# Time - O(n)
# Space - O(1)

        