class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 初始化三个指针
        p0 = 0  # 0 的右边界
        curr = 0  # 当前遍历指针
        p2 = len(nums) - 1  # 2 的左边界

        while curr <= p2:
            if nums[curr] == 0:
                # 交换当前元素和 p0 位置元素
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                # 交换当前元素和 p2 位置元素
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                # 遇到 1，直接跳过
                curr += 1
