class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        levelOrderList = []
        if root:
            queue.append((0,root))
            while(len(queue)!=0):
                level,element = queue.pop(0)
                if len(levelOrderList)-1 != level:
                    levelOrderList.append([])
                    levelOrderList[level].append(element.val)
                else:
                    levelOrderList[level].append(element.val)
                if element.left:
                    queue.append((level+1,element.left))
                if element.right:
                    queue.append((level+1,element.right))
        rightview = []
        if levelOrderList:
            for i in range(levelOrderList):
                rightview.append(levelOrderList[i].pop())
        return rightview
