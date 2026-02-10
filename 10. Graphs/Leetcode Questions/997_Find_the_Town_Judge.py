from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree_trust_in_me = [0] * (n + 1)
        outdegree_me_trust_others = [0] * (n + 1)

        for i, j in trust:
            indegree_trust_in_me[j] += 1
            outdegree_me_trust_others[i] += 1

        for i in range(1, n + 1):
            if indegree_trust_in_me[i] == n - 1 and outdegree_me_trust_others[i] == 0:
                return i

        return -1


# ------------------- DRIVER CODE -------------------
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    n = 2
    trust = [[1, 2]]
    print(sol.findJudge(n, trust))   # Expected: 2

    # Test Case 2
    n = 3
    trust = [[1, 3], [2, 3]]
    print(sol.findJudge(n, trust))   # Expected: 3

    # Test Case 3
    n = 3
    trust = [[1, 3], [2, 3], [3, 1]]
    print(sol.findJudge(n, trust))   # Expected: -1

    # Edge Case: Single person
    n = 1
    trust = []
    print(sol.findJudge(n, trust))   # Expected: 1
