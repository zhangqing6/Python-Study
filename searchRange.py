class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_left():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                # 找到目标值后，继续向左搜索，寻找第一个出现的位置
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            # 循环结束后，left 就是左边界，需要验证是否越界且值等于target
            if left >= len(nums) or nums[left] != target:
                return -1
            return left

        # 定义函数：找右边界
        def find_right():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                # 找到目标值后，继续向右搜索，寻找最后一个出现的位置
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            # 循环结束后，right 就是右边界，需要验证是否越界且值等于target
            if right < 0 or nums[right] != target:
                return -1
            return right

        # 调用两个函数获取结果
        left_pos = find_left()
        right_pos = find_right()
        return [left_pos, right_pos]
