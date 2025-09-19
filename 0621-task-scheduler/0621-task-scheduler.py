class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Neetcode - https://www.youtube.com/watch?v=s8p8ukTyA2I
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        # Create a minHeap to get the max value first(use -ve so you get max)
        # Create a queue to monitor whn the next A or B can be added back to minHeap
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            
            time += 1
            # Calculate heap = Reduce from A=3 to A=2 & append to q when next A can be added to maxHeap
            if maxHeap:
                rem = 1 + heapq.heappop(maxHeap)
                if rem:
                    q.append((rem, time + n))
        
            # # Calculate queue = When time matches the task
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

# Time Complexity: O(tasks * log 26) → O(tasks)

# Space Complexity: O(26 + n) → O(1)