class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                curr_val = board[row][col]
                if curr_val == ".":
                    continue
                box_index = (row // 3)*3 + (col // 3)
                if curr_val in rows[row] or curr_val in cols[col] or curr_val in boxes[box_index]:
                    return False
                rows[row].add(curr_val)
                cols[col].add(curr_val)
                boxes[box_index].add(curr_val)
        return True