class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        hashMap = {row:"" for row in range(1, numRows + 1)}
        top = True
        row = 1
        for char in s:    
            if row == 1 or (row < numRows and top):
                hashMap[row] += char
                print("if", hashMap[row])
                row += 1
                top = True
            else:
                hashMap[row] += char
                print("ELSE", hashMap[row])
                row -= 1
                top = False
        
        converted = ""
        for key, val in hashMap.items():
            converted += val
        
        return converted