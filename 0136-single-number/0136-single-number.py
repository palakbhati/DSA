class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        allXOR = 0

        for num in nums:
            allXOR = allXOR ^ num

        return allXOR
        