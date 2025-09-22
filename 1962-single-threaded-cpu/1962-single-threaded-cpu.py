class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Attach index to each task: (enqueueTime, processingTime, index)
        tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        tasks.sort()  # sort by enqueueTime

        res = []
        heap = []  # minHeap: (processingTime, index)
        time = 0
        i = 0  # pointer into sorted tasks

        while i < len(tasks) or heap:
            # If heap is empty, jump to next enqueueTime
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # Push all tasks available at 'time' into heap
            while i < len(tasks) and tasks[i][0] <= time:
                et, pt, idx = tasks[i]
                heapq.heappush(heap, (pt, idx))
                i += 1

            # Process next available task
            if heap:
                pt, idx = heapq.heappop(heap)
                time += pt
                res.append(idx)

        return res

# Total: O(n log n)
# Space: O(n) for heap and task list.