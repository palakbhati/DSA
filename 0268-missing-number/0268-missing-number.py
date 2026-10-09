class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        allXOR = 0

        for i in range(len(nums) + 1):
            allXOR = allXOR ^ i

        for num in nums:
            allXOR = allXOR ^ num

        return allXOR
        