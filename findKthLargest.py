class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)//大顶堆-num,用负数排序即可
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
