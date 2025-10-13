class Solution:
    def countDigits(self, num: int) -> int:

        temp = num
        count = 0

        while temp != 0:

            end_num = temp % 10
            if num % end_num == 0:
                count += 1
            
            temp //= 10
        
        return count

# Time - O(d) - d is the no of digits in num
# Space - O(1)
        