class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev,curr=0,0
        for num in nums:
            temp=curr
            curr=max(prev+num,curr)
            prev=temp
        return curr
