class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        res = []

        # set up hashmap for count
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        # set up heap (just append everything)
        # and pop off after it hits len(k)
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res