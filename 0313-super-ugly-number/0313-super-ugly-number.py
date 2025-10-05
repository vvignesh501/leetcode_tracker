class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = set([1])
        heap = [1]
        val = 1
        for _ in range(n):
            val = heapq.heappop(heap)
            for p in primes:
                nxt = val * p
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return val