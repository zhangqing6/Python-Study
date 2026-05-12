class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count=Counter(nums)
        heap=[]
        for num,freq in count.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq,num in heap ]
