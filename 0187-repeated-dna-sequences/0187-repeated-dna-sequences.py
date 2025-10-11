class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        k = 10
        dna = {}
        res = []

        for i in range(len(s)-k + 1):
            substring = s[i:i + k]

            if substring not in dna:
                dna[substring] = 1
            else:
                dna[substring] += 1
        
        for k, v in dna.items():
            if v > 1:
                res.append(k)
        return res