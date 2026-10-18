class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            j = target-nums[i]
            if (seen.get(j) is None):
                seen[nums[i]] = i
            else:
                return [seen[j], i]

        return []