from heapq import heappush, heappop
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        # Build max heap using negative values
        for n in nums:
            heappush(max_heap, -n)

        # Remove top k-1 elements
        for _ in range(k - 1):
            heappop(max_heap)

        # kth largest element
        return -heappop(max_heap)


# -------- TEST CASE --------
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

sol = Solution()
result = sol.findKthLargest(nums, k)
print("Kth Largest Element:", result)
