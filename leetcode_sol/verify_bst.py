
class Solution(object):
  
    def is_valid(self, root, floor=float('-inf'), ceiling= float('inf')):
        if not root:
          return True
        elif root.val <=floor or root.val >=ceiling:
          return False
        return self.is_valid(root.left,floor,root.val) and self.is_valid(root.right,root.val,ceiling)
      
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid(root,float('-inf'), float('inf'))
