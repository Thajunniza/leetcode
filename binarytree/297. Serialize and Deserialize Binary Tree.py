"""
297: Serialize and Deserialize Binary Tree

------------------------------------------------------------
Problem Statement:
------------------------------------------------------------
Design an algorithm to serialize and deserialize a binary tree. 
Serialization is the process of converting a tree to a string 
so that it can be stored or transmitted, and deserialization 
is converting the string back to the original tree structure.

Implement:
- Codec.serialize(root): Encodes a tree to a single string.
- Codec.deserialize(data): Decodes your encoded data to tree.

------------------------------------------------------------
Example:
------------------------------------------------------------
Input Tree:
        1
       / \
      2   3
         / \
        4   5

Serialized: "1,2,3,x,x,4,5"

Deserialization returns the same tree structure.

------------------------------------------------------------
Key Insight:
------------------------------------------------------------
- Use BFS to traverse the tree level by level.
- Use 'x' as placeholder for null children.
- Remove trailing 'x' values to avoid extra empty strings during deserialization.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    Codec class to serialize and deserialize a binary tree using BFS.
    """

    def serialize(self, root):
        """Encodes a tree to a single string using BFS."""
        if not root:
            return ""
        
        result = []
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("x")
        
        # Remove trailing 'x' values
        while result and result[-1] == "x":
            result.pop()
        
        return ",".join(result)

    def deserialize(self, data):
        """Decodes the encoded data to a tree using BFS."""
        if not data:
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while i < len(vals):
            parent = q.popleft()

            # Left child
            if vals[i] != "x":
                left = TreeNode(int(vals[i]))
                parent.left = left
                q.append(left)
            i += 1

            # Right child
            if i < len(vals) and vals[i] != "x":
                right = TreeNode(int(vals[i]))
                parent.right = right
                q.append(right)
            i += 1

        return root


# ------------------------------------------------------------
# Test Cases
# ------------------------------------------------------------
if __name__ == "__main__":
    # Test Case 1: Example tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)

    codec = Codec()
    serialized1 = codec.serialize(root1)
    print("Serialized Tree 1:", serialized1)
    deserialized_root1 = codec.deserialize(serialized1)
    print("Root Value:", deserialized_root1.val)
    print("Left Child:", deserialized_root1.left.val)
    print("Right Child:", deserialized_root1.right.val)
    print("Right Left Grandchild:", deserialized_root1.right.left.val)
    print("Right Right Grandchild:", deserialized_root1.right.right.val)

    # Test Case 2: Empty tree
    root2 = None
    serialized2 = codec.serialize(root2)
    print("Serialized Tree 2 (Empty):", serialized2)
    deserialized_root2 = codec.deserialize(serialized2)
    print("Deserialized Empty Tree:", deserialized_root2)

    # Test Case 3: Single node
    root3 = TreeNode(42)
    serialized3 = codec.serialize(root3)
    print("Serialized Tree 3 (Single Node):", serialized3)
    deserialized_root3 = codec.deserialize(serialized3)
    print("Deserialized Single Node Value:", deserialized_root3.val)

"""
------------------------------------------------------------
Time Complexity:
------------------------------------------------------------
- Serialize: O(n) for BFS traversal
- Deserialize: O(n) for BFS reconstruction

Space Complexity:
------------------------------------------------------------
- O(n) for queue and result list
"""