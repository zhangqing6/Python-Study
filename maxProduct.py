class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_dp=min_dp=res=nums[0]
        for num in nums[1:]:
            max_temp=max_dp
            min_temp=min_dp
            max_dp=max(num,max_temp*num,min_temp*num)
            min_dp=min(num,max_temp*num,min_temp*num)
            res=max(res,max_dp)
        return res
