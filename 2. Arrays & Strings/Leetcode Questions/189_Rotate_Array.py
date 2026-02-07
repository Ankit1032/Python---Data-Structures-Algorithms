class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        nums_size = len(nums)
        k = k % nums_size

        first_start = 0
        first_end = nums_size - k

        second_start = first_end
        second_end = nums_size

        if k!= nums_size:
            nums[:] = nums[second_start:second_end] + nums[first_start:first_end]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

sol = Solution()
sol.rotate(nums, k)

print(nums)