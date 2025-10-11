class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        # If 12 the avg of it is 4, as there are 3 elements, so 12 can be a target
        target = k * threshold
        curr_sum = sum(arr[:k])
        total = 0

        if curr_sum >= target:
            total += 1
        
        for i in range(k, len(arr)):
            # Remove the first element and add the next element to find the next subarray
            curr_sum += arr[i] - arr[i - k]
            if curr_sum >= target:
                total += 1
        
        return total


# Time - O(n)
# Space - O(1)
        