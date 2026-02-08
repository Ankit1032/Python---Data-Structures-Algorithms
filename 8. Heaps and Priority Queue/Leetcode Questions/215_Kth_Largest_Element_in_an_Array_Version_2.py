import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


# -------- TEST CASE --------
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

sol = Solution()
result = sol.findKthLargest(nums, k)
print("Kth Largest Element:", result)
