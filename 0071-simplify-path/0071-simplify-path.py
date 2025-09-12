class Solution:
    def simplifyPath(self, path: str) -> str:

        canonical = []
        splitPath = path.split('/')
        
        for char in splitPath:
            if char == '' or char == '.':
                continue
            elif char == '..':
                if canonical:
                    canonical.pop()
            else:
                canonical.append(char)
        

        # '/'.join(char for char in canonical) returns / within char not at the start
        return '/' + '/'.join(char for char in canonical)

# Time = O(n)
# Space = O(n)

        