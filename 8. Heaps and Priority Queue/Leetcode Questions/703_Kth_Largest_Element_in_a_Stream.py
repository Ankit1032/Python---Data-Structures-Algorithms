import heapq as hq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        # add initial numbers
        for i in nums:
            hq.heappush(self.heap, i)

        # keep heap size = k
        while len(self.heap) > self.k:
            hq.heappop(self.heap)

    def add(self, val: int) -> int:
        hq.heappush(self.heap, val)

        # keep heap size = k
        if len(self.heap) > self.k:
            hq.heappop(self.heap)

        # kth largest element
        return self.heap[0]


# -----------------------------
# Test Driver (Leetcode Style)
# -----------------------------
if __name__ == "__main__":

    operations = ["KthLargest", "add", "add", "add", "add"]
    inputs = [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

    obj = None
    output = []

    for op, inp in zip(operations, inputs):
        if op == "KthLargest":
            obj = KthLargest(inp[0], inp[1])
            output.append(None)
        else:
            res = obj.add(inp[0])
            output.append(res)

    print(output)
