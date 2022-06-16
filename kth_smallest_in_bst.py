"""
Inutition:
    Instead of doing DFS, storing the elements and then sorting them. Why not you directly do an inorder traversal.

DFS:
    Simple inoder traversal logic 
    Then return the k-1 th element from that returned list
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inOrder(node):
            return inOrder(node.left) + [node.val] + inOrder(node.right) if node else []
        
        return inOrder(root)[k-1]