class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        row index >= 0 essentially

        create pascal's triangle for every row until rowIndex + 1

        so if rowIndex == 0, then create pascal's triangle for the first row

        start with a list of lists


        """
        pascalTri = [[1], [1, 1]]
        # 1 + 1
        counter = 1
        while counter < rowIndex:
            tempRow = [1]
            left, right = 0, 1
            while right < len(pascalTri[counter]):
                tempVal = pascalTri[counter][left] + pascalTri[counter][right]
                tempRow.append(tempVal)
                left += 1
                right += 1
            tempRow.append(1)
            pascalTri.append(tempRow)
            counter += 1

        return pascalTri[rowIndex]
        
    # Time Complexity: O(nlog(n))
    # Space Complexity: O(nlog(n))



        