class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        plusOne = ""
        for d in digits:
            plusOne += str(d)
        
        output = str(int(plusOne) + 1)
        return list(map(int, output))

# Time - O(n)
# Space - O(n)