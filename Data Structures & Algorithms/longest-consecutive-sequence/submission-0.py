class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # left neighbor check
            if  (n - 1) not in numSet:
                length = 0
                # increment by 1 value check
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
                
        return longest