from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        positive_diagonal = set()   # r + c
        negative_diagonal = set()   # r - c

        res = []

        # Initialize board
        board = [["."] * n for _ in range(n)]

        def nqueen(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r + c) in positive_diagonal or (r - c) in negative_diagonal:
                    continue

                col.add(c)
                positive_diagonal.add(r + c)
                negative_diagonal.add(r - c)
                board[r][c] = "Q"

                nqueen(r + 1)

                col.remove(c)
                positive_diagonal.remove(r + c)
                negative_diagonal.remove(r - c)
                board[r][c] = "."

        nqueen(0)
        return res


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    n = 4
    result = sol.solveNQueens(n)
    print("n =", n)
    for soln in result:
        for row in soln:
            print(row)
        print()

    # Test case 2
    n = 1
    print("n =", n)
    print(sol.solveNQueens(n))
