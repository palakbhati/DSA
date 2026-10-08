class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set()
        lists = []
        for num in nums1:
            seen.add(num)

        for num in nums2:
            if num in seen and num not in lists:
                lists.append(num)
        
        return lists
                
        
        
        