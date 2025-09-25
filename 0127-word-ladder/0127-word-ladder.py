from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        L = len(beginWord)
        
        # Precompute wildcard forms
        wildcard_dict = defaultdict(list)
        for word in wordSet:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                wildcard_dict[pattern].append(word)
        
        # BFS
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while q:
            word, steps = q.popleft()
            
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                
                for neighbor in wildcard_dict.get(pattern, []):
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, steps + 1))
                
                # Optional: clear to prevent revisiting
                wildcard_dict[pattern] = []
        
        return 0

# Time: O(N * L)
# Space O(N*L)