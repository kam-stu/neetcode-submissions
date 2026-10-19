class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        # create hashmap (value : count)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # append all elements frequenecy array (index => count; value at index => value in nums)
        for val, count in count.items():
            freq[count].append(val)
        
        res = []
        # pop off the top k elements (going from r -> l)
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
