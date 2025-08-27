class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequentMap = {}
        output = []
        for n in nums:
            frequentMap[n] = frequentMap.get(n, 0) + 1

        sorted_dictionary = sorted(frequentMap.items(), key=lambda x:x[1], reverse=True)

        for key, value in sorted_dictionary:
            if k!= 0:
                output.append(key)
                k -= 1
        
        return output

# Time = O(n)
# Space = O(n)
        