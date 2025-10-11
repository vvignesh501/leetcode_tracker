class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        k = 10
        dna = {}
        res = []

        for i in range(len(s)- k + 1):
            substring = s[i:i + k]
            dna[substring] = 1 + dna.get(substring, 0)
        
        for k, v in dna.items():
            if v > 1:
                res.append(k)
        return res

# Time - O(n)
# Space - O(n)