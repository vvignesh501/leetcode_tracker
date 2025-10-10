class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        total = sum(arr)
        avg = total // 3
        count = 0
        curr_sum = 0

        if total % 3 != 0:
            return False

        for i in range(len(arr)):
            curr_sum += arr[i]

            if curr_sum == avg:
                count += 1
                curr_sum = 0
            
            if count == 3:
                return True
        
        return False

# Time - O(n)
# Space - O(1)