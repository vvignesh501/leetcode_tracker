class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        res = ""
        prev = None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            cnt += 1
            res += char

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return res

# Time - O(nlogk)
# Space: O(k) for heap + result string.
        