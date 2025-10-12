class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        res = []

        for i in range(len(nums)):

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            # Remove the index in queue, if index is behind the k value.
            # i.e the sliding window went past the k=3. (i = 3, k =3) (i-k = 0th index)
            if queue[0] <= i - k:
                queue.popleft()

            # Append max when window size is reached
            if i >= k - 1:
                res.append(nums[queue[0]])
        
        return res
        