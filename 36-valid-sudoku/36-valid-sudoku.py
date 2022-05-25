class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # visited sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # iterate through the board:
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                
                # if no value, move on
                if val == '.':
                    continue
                    
                # validate row
                if val in rows[row]:
                    return False
                rows[row].add(val)
                
                # validate col
                if val in cols[col]:
                    return False
                cols[col].add(val)
                
                # validate square
                box = (row // 3) * 3 + col // 3
                if val in boxes[box]:
                    return False
                boxes[box].add(val)
                
        return True
