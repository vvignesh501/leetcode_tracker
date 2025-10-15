class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Sort each word. Use hashmap[sorted_word] += word
        # Now all sorted words are in hashmap
        
        hashmap = collections.defaultdict(list)
        
        for char in strs:
            sorted_char = ''.join(sorted(char))
            print(sorted_char)
            if sorted_char in hashmap:
                hashmap[sorted_char].append(char)
            else:
                hashmap[sorted_char] = [char]
        
        return list(hashmap.values())


        # Solution 2 

        # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #     res = defaultdict(list)
        #     for s in strs :
        #         count = ['0'] * 26
        #         for c in s :
        #             oldVal = int(count[ord(c) - ord('a')])
        #             count[ord(c) - ord('a')] = str(oldVal+1)
        #         res[','.join(count)].append(s)
        #     return res.values()