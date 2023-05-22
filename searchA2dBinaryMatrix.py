class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left, right = 0, len(matrix)-1

        while left <= right:
            mid = (left+right)//2

            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][len(matrix[mid])-1] < target:
                left = mid + 1
            else:
                left += 1
                
            # after those 2 if-statements, we are on the correct row

            current_row = matrix[mid]
            l, r = 0, len(current_row)-1

            while l <= r:
                m = (l+r)//2

                if current_row[m] == target:
                    return True
                elif current_row[m] > target:
                    r = m - 1
                elif current_row[m] < target:
                    l = m + 1

        return False