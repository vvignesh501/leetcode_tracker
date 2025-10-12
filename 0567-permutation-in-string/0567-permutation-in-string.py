from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_count = Counter(s1)
        window_count = Counter()

        for i, char in enumerate(s2):
            window_count[char] += 1

            if i >= k:
                # remove the leftmost character as window slides
                left_char = s2[i - k]
                if window_count[left_char] == 1:
                    del window_count[left_char]
                else:
                    window_count[left_char] -= 1

            if window_count == s1_count:
                return True
        
        return False
