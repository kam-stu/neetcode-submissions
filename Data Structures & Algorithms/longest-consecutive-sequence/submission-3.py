class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 0
        nums_set = set(nums)
        for i in range(len(nums)):
            if (nums[i]-1) not in nums_set:
                count = 1
                next_num = nums[i]+1
                while (next_num in nums_set):
                    count += 1
                    next_num += 1
                curr = max(curr, count)
        return curr