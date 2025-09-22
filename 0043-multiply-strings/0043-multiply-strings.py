class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)
        
        # multiply each digit
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                summ = mul + res[p2]
                
                res[p2] = summ % 10
                res[p1] += summ // 10
        
        # convert to string
        result = ''.join(map(str, res))
        return result.lstrip('0')

# Time: O(m * n) → each digit in num1 multiplies each digit in num2

# Space: O(m + n) → result array