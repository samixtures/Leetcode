# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        has at least 1 node, and at max 1000

        I'd like an iterative bfs, or level order traversal

        A small, but important, note is when we are on a certain level
        we should use a start and end pointer at index 0 and the final index,
        and we should check if they're equal, and then move them both closer
        towards the middle, until start > end. That also means that if there
        isn't a node somewhere we should indicate that by adding "None"
        to the list we will be using to compare the values in a level.

        This is because None, 3, 3, None is symmetric, but
        None, 3, None, 3 is not symmetric, and it's going to register
        as symmetric unless we add the Nones.

        Iterative BFS:
        createt a queue with the root in it,
        pop the first value in the queue, save it in a variable
        check if it has left and right values, if it does add them to the back
        of the queue, if it doesn't, add None in their place,

        then, after we've completed 
        """
        q = [root]
        while len(q) > 0:
            lengthQ = len(q)

            while lengthQ > 0:
                currNode = q.pop(0)
                # print("currNode is", currNode)
                if currNode != None:
                    if currNode.left:
                        q.append(currNode.left)
                    else:
                        q.append(None)
                    if currNode.right:
                        q.append(currNode.right)
                    else:
                        q.append(None)
                lengthQ -= 1
                print("Length", lengthQ)

                for x in q:
                    if x:
                        print(x.val)
                    else:
                        print("None")

                start = 0
                end = len(q)-1
                while start < end:
                    print(q[start].val, q[end].val)
                    if len(q) > 0:
                        if q[start].val == q[end].val:
                            start += 1
                            end -= 1
                        else:
                            return False
                    else:
                        break
        return True
        
            
                    