# Day 6
# Insert into a Binary Search Tree

#You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

#Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

#Example 1:
#Input: root = [4,2,7,1,3], val = 5
#Output: [4,2,7,1,3,5]
#Explanation: Another accepted tree is:


#Example 2:
#Input: root = [40,20,60,10,30,50,70], val = 25
#Output: [40,20,60,10,30,50,70,null,null,25]


#Example 3:
#Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
#Output: [4,2,7,1,3,5]


#Constraints:
#The number of nodes in the tree will be in the range [0, 104].
#-108 <= Node.val <= 108
#All the values Node.val are unique.
#-108 <= val <= 108
#It's guaranteed that val does not exist in the original BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root==None:
            return TreeNode(val)
        
        prev = None
        temp = root
        
        while temp!=None:
            prev = temp
            if val<temp.val:
                temp = temp.left
                
            elif val>temp.val:
                temp = temp.right
        
        if val<prev.val:
            prev.left = TreeNode(val)
        
        else:
            prev.right = TreeNode(val)
        
        return root
        
#        if root == None: 
#            return TreeNode(val)
        
#        current_node = root
#        while(True):
#            if current_node.val <= val and current_node != null:
#                current_node = current_node.right
#            elif current_node.val <= val and current_node == None:
#                current_node.right = TreeNode(val)
#                break
#            elif current_node.val >= val and current_node.left != None:
#                current_node = current_node.left
#            elif current_node.val >= val and current_node.left == None:
#                current_node.left = TreeNode(val)
#                break
        
#        return root
                