class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
t = TreeNode(4, TreeNode(2),  TreeNode(7, TreeNode(6), TreeNode(8)))
print(t.left.val)

def dfs(root: TreeNode):
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                print(node.val)
            if node:
                stack.append(node.left)
                stack.append(node.right)
        return
    
# .pop() removes from right side (i didn't realize that lol)

dfs(t)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# t = TreeNode(4, TreeNode(2),  TreeNode(7, TreeNode(6), TreeNode(8)))

# def dfs(t, value):
#     s = [t]
#     while s:
#         node = s.pop(0)
#         # print(node.val)
#         if node.val == value:
#             return node
#         if node.left:
#             s.insert(0, node.left)
#         if node.right:
#             s.insert(0, node.right)
#         for x in s:
#             print(x.val, end =" ")
#         print("")
#     return 
# dfs(t, 2)