# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        allBoard = []
        def dfs(node,list):
            if not node.left and not node.right:
                if sum(list) == targetSum:
                    temp = list.copy()
                    allBoard.append(temp)
                return  
            if node.left:
                list.append(node.left.val)
                dfs(node.left,list)
                list.pop()
            if node.right:
                list.append(node.right.val)
                dfs(node.right,list)
                list.pop()
        if root:
            list = []
            list.append(root.val)
            dfs(root,list)
        return allBoard
    
root = TreeNode(5,TreeNode(4,None,None),TreeNode(6,None,None))
obj = Solution()
print(obj.pathSum(root,11))
