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