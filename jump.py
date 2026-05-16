class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps=0
        current_end=0
        max_run=0
        for i in range(len(nums)-1):
            max_run=max(max_run,i+nums[i])
            if i==current_end:
                jumps+=1
                current_end=max_run
                if current_end>=len(nums)-1:
                    break
        return jumps
