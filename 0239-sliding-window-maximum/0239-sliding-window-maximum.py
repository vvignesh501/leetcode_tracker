class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = 0
        queue = deque()
        res = []

        for r in range(len(nums)):

            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            # Pop only when left = queue[0]
            if r - l + 1 > k:
                if queue and queue[0] == l:
                    queue.popleft()
                l += 1

            # Append max when window size 3 is reached
            if r - l + 1 == k:
                res.append(nums[queue[0]])
        
        return res
        