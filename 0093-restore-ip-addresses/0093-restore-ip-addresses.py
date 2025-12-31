class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        final = []
        comb = []
        
        if len(s) < 4 or len(s) > 16:
            return []
        
        def backtracking(s, ind):
            
            if len(comb)==4 and len(''.join(comb)) == len(s):
                final.append('.'.join(comb[:]))
                return 
            
            for ii in range(ind, len(s)):
                tmp_str = s[ind:ii+1]
                if self.isvalid(tmp_str):
                    comb.append(tmp_str)
                    backtracking(s,ii+1)
                    comb.pop()
        backtracking(s,0)
        return final

    
    def isvalid(self, tmp_str):
        if len(tmp_str) < 1:
            return False
        if len(tmp_str) > 4:
            return False
        if tmp_str[0] == "0" and len(tmp_str)>1:
            return False
        if int(tmp_str) > 255:
            return False
        return True

# Time - O