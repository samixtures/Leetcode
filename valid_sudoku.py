class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Initial thoughts:
        sets are good for checking duplicates
        
        check if all the values on each row are unique
        check if all the values on each column are unique
        """

        # CHECKS FOR DUPLICATES IN COLUMNS
        for x in range(9):
            char_set = set()
            for y in range(9):
                if board[y][x] != ".":
                    if board[y][x] in char_set:
                        return False
                    else: char_set.add(board[y][x])
        # CHECKS FOR DUPLICATES IN ROWS
        for x in range(9):
            char_set = set()
            for y in range(9):
                if board[x][y] != ".":
                    if board[x][y] in char_set:
                        return False
                    else: char_set.add(board[x][y])
    
        # CHECKS FOR DUPLICATES IN 3X3s
        # the left three 3x3s
        char_set = set()
        for x in range(9):
            if x % 3 == 0:
                char_set = set()
            for y in range(3):
                if board[x][y] != ".":
                    if board[x][y] in char_set:
                        return False
                    else: char_set.add(board[x][y])
        # the middle three 3x3s
        char_set = set()
        for x in range(9):
            if x % 3 == 0:
                char_set = set()
            for y in range(3, 6):
                if board[x][y] != ".":
                    if board[x][y] in char_set:
                        return False
                    else: char_set.add(board[x][y])
        # the right three 3x3s
        char_set = set()
        for x in range(9):
            if x % 3 == 0:
                char_set = set()
            for y in range(6, 9):
                if board[x][y] != ".":
                    if board[x][y] in char_set:
                        return False
                    else: char_set.add(board[x][y])
    
        return True