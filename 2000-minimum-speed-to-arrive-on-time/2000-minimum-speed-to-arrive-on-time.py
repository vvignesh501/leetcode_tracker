class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        l = 1
        r = 10 ** 7
        res = -1

        while l <= r:
                
            total = 0
            mid = (l + r) // 2

            # Every train needs a roundup, except the last
            for i in range(len(dist)-1):
                total += math.ceil(dist[i]/mid)
            total += dist[-1]/mid
            
            if total > hour:
                l = mid + 1
            elif total <= hour:
                res = mid
                r = mid - 1
        
        return res
        