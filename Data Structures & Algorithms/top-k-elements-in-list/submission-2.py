class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k=2
        # nums = [3,1,2,2,3]
        # count = {3:2, 1:1, 2:2}
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        # arr = [[1,1], [2,3], [2,2]]
        res = [] 
        while len(res) < k:
            res.append(arr.pop()[1])
        # res = [2, 3]
        return res


        