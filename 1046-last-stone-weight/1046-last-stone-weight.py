class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Convert all the elements to negative as it is minHeap
        # Max heap can be got making all elements negative
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones)  > 1:

            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, first - second)
        
        return -stones[0] if stones else 0

# Time: O(n log n)

# Space: O(n)     