class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_set = set(nums)
        return (len(dupe_set) != len(nums))