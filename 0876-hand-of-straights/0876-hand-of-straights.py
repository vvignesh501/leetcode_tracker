class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for card in sorted(count):  # always take smallest card available
            while count[card] > 0:  # need to build a group starting here
                for i in range(groupSize):
                    if count[card + i] == 0:
                        return False
                    count[card + i] -= 1
                    
        return True

# Time: O(n log n)
# Space: O(n)