class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using heap sol
        res = []

        count = {}

        # setup hashmap with num : count
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # setup minheap with value: (count, num)
        # if heap length > k, pop it off (essentially turning it into a max heap)
        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, (cnt, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])


        return res