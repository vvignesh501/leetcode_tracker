class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = []

        while i < len(chars):
            res.append(chars[i])
            count = 1
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                i += 1
                count += 1

            if count > 1:
                for c in str(count):
                    res.append(c)
            i += 1

        # Modify the input array in place
        for j in range(len(res)):
            chars[j] = res[j]

        return len(res)


# Time: O(n)

# Space: O(1) (in-place modification)