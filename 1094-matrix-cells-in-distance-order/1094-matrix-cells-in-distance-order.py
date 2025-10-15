class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        answer = []
        
        for i in range(rows):
            for j in range(cols):
                answer.append([i,j])
        
        answer.sort(key=lambda x: abs(x[0]- rCenter) + abs(x[1] - cCenter))
        
        return answer

# Time - O(m * n)
# Space - O(m + n)