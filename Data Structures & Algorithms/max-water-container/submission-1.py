class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights)-1

        while l < r:
            distance = r - l
            curr_height = min(heights[l], heights[r])
            res = max(res, distance*curr_height)

            # increment/decrement pointers
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return res