class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []  # stores pairs [index, temperature]

        for idx, temp in enumerate(temperatures):
            # resolve previous days waiting for warmer temperature
            while stack and temp > stack[-1][1]:
                prev_idx, prev_temp = stack.pop()
                result[prev_idx] = idx - prev_idx
            stack.append([idx, temp])

        return result

# time = O(n)
# space = O(n)
        