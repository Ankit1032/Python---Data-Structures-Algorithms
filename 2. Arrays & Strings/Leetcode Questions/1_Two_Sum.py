from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr_dict = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in arr_dict:
                return [i, arr_dict[diff]]
            else:
                arr_dict[nums[i]] = i

        return []


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # Expected: [1, 0] or [0, 1]

    # Test Case 2
    nums = [3, 2, 4]
    target = 6
    print(sol.twoSum(nums, target))  # Expected: [2, 1]

    # Test Case 3
    nums = [3, 3]
    target = 6
    print(sol.twoSum(nums, target))  # Expected: [1, 0]
