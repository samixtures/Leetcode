class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTri = [[1]]
        if numRows == 1:
            return pascalTri
        
        # 5
        # append 1, use 2 pointers to append numbers right next to each other
        # and append those sums, then append 1 at the end

        index = 0
        while index+1 < numRows:
            newRow = [1]
            left, right = 0, 1
            while right < len(pascalTri[index]):
                currVal = pascalTri[index][left] + pascalTri[index][right]
                newRow.append(currVal)
                left += 1
                right += 1
            newRow.append(1)
            pascalTri.append(newRow)
            index += 1
        return pascalTri
    # Time Complexity: O(nlog(n)) -> where n == numRows we iterate that many
    #   times, and within each iteration we iterate less than that many times
    #   until the last iteration.
    # Space Complexity: O(nlog(n)) -> where n == numRows we have that many
    #   items in a nested list, but the number of elements within each smaller
    #   list is smaller than n, except for the last last