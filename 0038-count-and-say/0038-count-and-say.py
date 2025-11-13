class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"


        # Think it in real conversation terms 
        # result.append(str(count) + term[i]) = when you say it's 1 in string + 1
        def next_term(term: str) -> str:
            result = []
            i = 0
            while i < len(term):
                count = 1
                # Eg - aaabb, count until it's aaa and when it changes to aaab append the count
                while i + 1 < len(term) and term[i] == term[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count) + term[i])
                i += 1
            return ''.join(result)

        term = "1"
        for _ in range(2, n + 1):
            term = next_term(term)
        
        return term
