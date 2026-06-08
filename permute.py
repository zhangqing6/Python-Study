class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        n=len(nums)
        used=[False]*n
        def backtrack(path):
            if len(path)==n:
                result.append(list(path))
                return
            for i in range(n):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i]=False
        backtrack([])
        return result
