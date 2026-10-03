class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequencyMap = {}
        for char in s:
            if char in frequencyMap:
                frequencyMap[char] += 1
            else:
                frequencyMap[char] = 1

        for char in t:
            if char not in frequencyMap:
                return False
        

            frequencyMap[char] -= 1
            
            if frequencyMap[char] < 0:
                return False
                
        return True


            

    
    