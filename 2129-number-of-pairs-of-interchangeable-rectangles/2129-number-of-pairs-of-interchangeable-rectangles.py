class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:

        pairs = {}

        for pair in rectangles:
            w, h = pair[0], pair[1]
            pairs[w/h] = 1 + pairs.get(w/h, 0)
        
        res = 0
        for v in pairs.values():
            res += (v * (v-1)) // 2
        
        return res
        