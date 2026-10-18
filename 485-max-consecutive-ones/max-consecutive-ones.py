class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count= 0
        max_consecutive_count = 0 
        for num in nums:
            if num == 1:
                count += 1 
                max_consecutive_count = max(max_consecutive_count, count)
            else:
                count = 0

        return max_consecutive_count