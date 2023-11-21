class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def board_set_index(i, j):
            if i <= 2 and j <= 2:
                return 0
            elif i <= 2 and j <= 5:
                return 1
            elif i <= 2 and j <= 8:
                return 2
            elif i <= 5 and j <= 2:
                return 3
            elif i <= 5 and j <= 5:
                return 4
            elif i <= 5 and j <= 8:
                return 5
            elif i <= 8 and j <= 2:
                return 6
            elif i <= 8 and j <= 5:
                return 7
            else:
                return 8

        board_set = [[] for i in range(9)]
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        for iind, i in enumerate(board):
            for jind, j in enumerate(i):
                if j != '.':
                    row[iind].append(int(j))
                    col[jind].append(int(j))
                    bind = board_set_index(iind, jind)
                    board_set[bind].append(int(j))
        
        for i in row:
            if len(i) != len(set(i)):
                return False
        
        for i in col:
            if len(i) != len(set(i)):
                return False
        
        for i in board_set:
            if len(i) != len(set(i)):
                return False

        return True