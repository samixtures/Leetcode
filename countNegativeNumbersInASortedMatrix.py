class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for x in grid:
            for y in x:
                if y < 0:
                    counter += 1
        return counter