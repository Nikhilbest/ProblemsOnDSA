class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)

        # check for letter in dictionary, increase count
        for letter in s:
            d[letter] += 1
        
        for letter in t:
            d[letter] -= 1

        # difference should be 0, if match all count
        for key in d.values():
            if key != 0:
                return False
        return True
        
