class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        MAX_BOX_ROW = 3
        MAX_BOX_COL = 3
        MAX_DIGIT = 9
        boxes_map = {}
        rows_map = {}
        cols_map = {}

        # Iterates Rows
        for row, rowEls in enumerate(board):
            box_row_idx = row // MAX_BOX_ROW
            #Iterates Cols
            for col, columnEl in enumerate(rowEls):
                if columnEl == '.':
                    continue
                # Check Box
                box_col_idx = col // MAX_BOX_COL
                box_key = tuple([box_row_idx, box_col_idx])
                elIdx = int(columnEl) - 1
                if box_key not in boxes_map:
                    boxes_map[box_key] = [0] * MAX_DIGIT
                boxes_map[box_key][elIdx] = boxes_map.get(box_key)[elIdx] + 1
                if boxes_map.get(box_key)[elIdx] == 2:
                    return False
                
                # Check Row
                if row not in rows_map:
                    rows_map[row] = [0] * MAX_DIGIT
                rows_map[row][elIdx] = rows_map.get(row)[elIdx] + 1
                if rows_map.get(row)[elIdx] == 2:
                    return False
                
                # Check Column
                if col not in cols_map:
                    cols_map[col] = [0] * MAX_DIGIT
                cols_map[col][elIdx] = cols_map.get(col)[elIdx] + 1
                if cols_map.get(col)[elIdx] == 2:
                    return False
        
        return True