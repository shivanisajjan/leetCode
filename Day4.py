# https://leetcode.com/problems/valid-sudoku/submissions/


# #### Note: Using Dictionary gives best results. check below solution

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            li = {}
            for j in range(9):
                if board[i][j] != ".":
                    if li.get(board[i][j]):
                        return False
                    else:
                        li[board[i][j]] = True
        for i in range(0, 9):
            li = {}
            for j in range(0, 9):
                if board[j][i] != ".":
                    if li.get(board[j][i]):
                        return False
                    else:
                        li[board[j][i]] = True
        for i in range(0, 3):
            for j in range(0, 3):
                li = {}
                for k in range(i * 3, (i * 3) + 3):
                    for l in range(j * 3, (j * 3) + 3):
                        if board[k][l] != ".":
                            if li.get(board[k][l]):
                                return False
                            else:
                                li[board[k][l]] = True
        return True
