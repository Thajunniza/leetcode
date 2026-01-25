# vertical_order_bfs.py

"""

------------------------------------------------------------
987 - Vertical Order Traversal of a Binary Tree
------------------------------------------------------------
Given a binary tree, return the vertical order traversal of its nodes' values.

- Nodes are reported column by column, from leftmost column to rightmost.
- Nodes in the same column are reported top-to-bottom.
- Nodes in the same row and column appear in **left-to-right order** as in BFS traversal.

------------------------------------------------------------
Example:
------------------------------------------------------------
Input:
       3
      / \
     9   20
         / \
        15  7

Output:
[[9], [3, 15], [20], [7]]

Explanation:
- Column -1: [9]
- Column 0: [3, 15] (3 is above 15)
- Column 1: [20]
- Column 2: [7]
"""

from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    # Dictionary to store nodes grouped by column
    vert = defaultdict(list)

    # BFS queue: (node, column, row)
    q = deque([(root, 0, 0)])

    while q:
        node, col, row = q.popleft()
        # Store row and node itself
        vert[col].append((row, node))

        # Add children to the queue
        if node.left:
            q.append((node.left, col - 1, row + 1))
        if node.right:
            q.append((node.right, col + 1, row + 1))

    result = []

    # Process columns from left to right
    for col in sorted(vert):
        # Sort by row only; BFS preserves left-to-right for same row
        vert[col].sort(key=lambda x: x[0])
        # Extract node values
        result.append([node.data for row, node in vert[col]])

    return result


# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    # Construct tree:
    #       3
    #      / \
    #     9   20
    #         / \
    #        15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(vertical_order(root))
    # Expected output: [[9], [3, 15], [20], [7]]


"""
------------------------------------------------------------
Time Complexity:
------------------------------------------------------------
- BFS visits each node once: O(n)
- Sorting nodes in each column: O(k log k) for k nodes per column
- Total worst-case: O(n log n), if all nodes are in the same column

------------------------------------------------------------
Space Complexity:
------------------------------------------------------------
- BFS queue stores up to n nodes: O(n)
- Column dictionary stores all nodes: O(n)
- Result list: O(n)
- Total: O(n)
"""