class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count how many times each element appears; value : count
        count = {}
        
        # array to map out how many times each number shows up; index => count; index at value => [num(s)]
        freq = [[] for i in range(len(nums)+1)]

        # set up hashmap
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        # set up arr
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        # main loop - want to loop through array in descending order and get every value until 
        # len(res) == k (we have the kth most elements)
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res