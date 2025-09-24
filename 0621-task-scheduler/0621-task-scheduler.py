from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # stores pairs: (ready_time, count)

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # run the most frequent task
                if cnt != 0:
                    # push into cooldown queue: available again at time+n
                    q.append((time + n, cnt))

            if q and q[0][0] == time:  # task ready to be re-added
                heapq.heappush(maxHeap, q.popleft()[1])

        return time

# Time Complexity: O(T log k) → since k ≤ 26, this is effectively O(T).

# Space Complexity:

# Counter: O(k)

# Heap: O(k)

# Queue: O(k)
# → O(k) ≈ O(1) (bounded by 26).