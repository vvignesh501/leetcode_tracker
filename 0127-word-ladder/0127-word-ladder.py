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
        q = deque([beginWord])
        visited = set([beginWord])
        steps = 1
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for neighbour in wildcard_dict[pattern]:
                        
                        if neighbour == endWord:
                            return steps + 1

                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)
            steps += 1
            
        return 0



# Time: O(N * L)
# Space O(N*L)