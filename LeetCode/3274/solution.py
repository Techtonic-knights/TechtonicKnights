class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def is_square_white(coordinate):
            if ord(coordinate[0])% 2 == int(coordinate[1]) % 2 :
                return False
            return True
        return is_square_white(coordinate1) == is_square_white(coordinate2)
