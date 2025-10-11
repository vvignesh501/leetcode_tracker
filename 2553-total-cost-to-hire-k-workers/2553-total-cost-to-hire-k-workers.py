import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        total = 0
        
        # Two pointers
        l, r = 0, n - 1
        
        left_heap, right_heap = [], []
        
        # Fill initial heaps
        for _ in range(candidates):
            if l <= r:
                heapq.heappush(left_heap, costs[l])
                l += 1
            if l <= r:
                heapq.heappush(right_heap, costs[r])
                r -= 1
        
        for _ in range(k):
            # Choose cheaper of two sides
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total += heapq.heappop(left_heap)
                if l <= r:
                    heapq.heappush(left_heap, costs[l])
                    l += 1
            else:
                total += heapq.heappop(right_heap)
                if l <= r:
                    heapq.heappush(right_heap, costs[r])
                    r -= 1
        
        return total


# Time	O(k log candidates)	Each hire pops + pushes 1 item (log c) from a heap of ≤ candidates
# Space	O(candidates)	Two heaps of size ≤ candidates each