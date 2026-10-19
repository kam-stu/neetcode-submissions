class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for i in range(len(nums)):
            if (nums[i]-1 in num_set):
                continue
            curr = 0
            next_num = nums[i]
            while (next_num in num_set):
                curr += 1
                res = max(res, curr)
                next_num += 1
        
        return res
