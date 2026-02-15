from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, word_len_index):

            if word_len_index == len(word):
                return True

            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or
                board[r][c] != word[word_len_index]
            ):
                return False

            visited.add((r, c))

            res = (
                dfs(r + 1, c, word_len_index + 1) or
                dfs(r - 1, c, word_len_index + 1) or
                dfs(r, c - 1, word_len_index + 1) or
                dfs(r, c + 1, word_len_index + 1)
            )

            visited.remove((r, c))

            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sol = Solution()

    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]

    # Test Case 1
    word = "ABCCED"
    print(f'Word "{word}" exists:', sol.exist(board, word))  # Expected: True

    # Test Case 2
    word = "SEE"
    print(f'Word "{word}" exists:', sol.exist(board, word))  # Expected: True

    # Test Case 3
    word = "ABCB"
    print(f'Word "{word}" exists:', sol.exist(board, word))  # Expected: False
