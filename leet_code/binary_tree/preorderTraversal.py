#Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree. Here is an example:

class TreeNode():
    def __init__(self, val=0, left_node = None, right_node = None):
        self.val = val
        self.left = left_node
        self.right = right_node

# My solution
class Solution:

    def preorderTraversal(self, root: TreeNode):
        return self.__traverse(root)

    def __traverse(self, node: TreeNode):
        tree_list = []
        if node is None:
            return
        tree_list.append(node.val)
        if node.left_node is not None:
            tree_list = tree_list + self.__traverse(node.left_node)
            
        if node.right_node is not None:
            tree_list = tree_list + self.__traverse(node.right_node)

        return tree_list

# LeetCode solution
class Solution_Leet:
    def preorderTraversal(self, root: TreeNode):
        
        ans = []
        self.__traverse(root, ans)
        return ans
        
    def __traverse(self, root, ans):
        
        if not root:
            return
        
        ans.append(root.val)
        self.__traverse(root.left, ans)
        self.__traverse(root.right, ans)        

if __name__ == "__main__":
    root = [1,None,2,3]
    root_tree = TreeNode(root[0])
    root_tree.right = TreeNode(root[2])
    root_tree.right.left = TreeNode(root[3])
    binary_tree = Solution()
    print(binary_tree.preorderTraversal(root_tree))
    print(binary_tree.preorderTraversal(None))
    print(binary_tree.preorderTraversal(TreeNode(1)))
