class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        # get the count of each element in nums
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # map out the array where index: count of the element, value: array of all elements that has that count
        for num, cnt in count.items():
            freq[cnt].append(num)

        # have all the elements in place, can now safely loop through array backwards and grab all elements
        # we can stop once len(res) == k since that is always bound to happen
        res = []

        for i in range(len(freq)-1, 0, -1):
            # since there can be multiple values in the value-array
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res