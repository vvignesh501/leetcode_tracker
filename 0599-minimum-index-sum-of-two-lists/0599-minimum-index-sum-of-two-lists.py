class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        least_sum = float("inf")
        res = []

        list1Hash = {s: i for i, s in enumerate(list1)}

        for j, s in enumerate(list2):

            if list2[j] in list1Hash:
                total = j + list1Hash[s]

                if total < least_sum:
                    least_sum = total    
                    res = [s]
                elif total == least_sum:
                    res.append(s)
        
        return res

# Time = O(n)
# Space - O(n)
