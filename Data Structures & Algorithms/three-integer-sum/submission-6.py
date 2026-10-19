class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            
            # don't want to repeat numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # if nums[i] > 0, there can physically be no other combination that works
            if nums[i] > 0:
                break

            l,r = i+1, len(nums)-1

            while l < r:
                three_some = nums[i] + nums[l] + nums[r]

                if three_some > 0:
                    r -= 1
                elif three_some < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            
        return res