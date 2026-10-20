class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0

        for i in range(len(nums)):
            
            # already looked for the seq
            if nums[i]-1 in num_set:
                continue
            curr = nums[i]
            running = 0
            while curr in num_set:
                running += 1
                curr += 1
                count = max(count, running)
        
        return count