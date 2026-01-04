"""
===========================================================
707. Design Linked List
===========================================================

🧩 Problem:
Design your implementation of the linked list. You can choose to use a singly or 
doubly linked list.

A node in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference to the next node.

Implement the MyLinkedList class:
- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the index-th node in the linked list. 
  If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of 
  the linked list. After the insertion, the new node will be the first node of 
  the linked list.
- void addAtTail(int val) Append a node of value val as the last element of 
  the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the index-th 
  node in the linked list. If index equals the length of the linked list, the node 
  will be appended to the end of the linked list. If index is greater than the 
  length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the index-th node in the linked list, 
  if the index is valid.

-----------------------------------------------------------
Example :
-----------------------------------------------------------
Input:
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]

Output:
[null, null, null, null, 2, null, 3]

Explanation:
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

-----------------------------------------------------------
🧠 Approach: Singly Linked List with Dummy Head
-----------------------------------------------------------
Data Structure:
- Node class with val and next attributes
- Use a dummy head node to simplify edge cases
- Keep track of size for efficient validation

Why Dummy Head?
- Eliminates special cases for operations at head
- Simplifies insertion and deletion logic
- Makes code cleaner and less error-prone

Algorithm:

1. Initialization:
   - Create a dummy head node (sentinel node)
   - Initialize size to 0
   
2. get(index):
   - Validate index (0 <= index < size)
   - Traverse from dummy.next to index-th node
   - Return node value or -1 if invalid
   
3. addAtHead(val):
   - Create new node
   - Insert after dummy head
   - Increment size
   
4. addAtTail(val):
   - Traverse to last node
   - Append new node
   - Increment size
   
5. addAtIndex(index, val):
   - Validate index (0 <= index <= size)
   - Traverse to (index-1)-th node
   - Insert new node after it
   - Increment size
   
6. deleteAtIndex(index):
   - Validate index (0 <= index < size)
   - Traverse to (index-1)-th node
   - Remove index-th node by updating pointers
   - Decrement size

-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  
- get(index): O(index) = O(n)
- addAtHead(val): O(1)
- addAtTail(val): O(n)
- addAtIndex(index, val): O(index) = O(n)
- deleteAtIndex(index): O(index) = O(n)

Space: O(1) for all operations (excluding the space for nodes)

"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        """
        Initialize the linked list with a dummy head node.
        """
        self.head = Node(0)  # Dummy head
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # Validate index
        if index < 0 or index >= self.size:
            return -1
        
        # Traverse to the index-th node
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val as the last element.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node.
        If index equals size, append to the end.
        If index > size, don't insert.
        :type index: int
        :type val: int
        :rtype: None
        """
        # Validate index
        if index > self.size:
            return
        
        # Allow negative index to be treated as 0
        if index < 0:
            index = 0
        
        # Traverse to the (index-1)-th node
        prev = self.head
        for i in range(index):
            prev = prev.next
        
        # Insert new node
        new_node = Node(val)
        new_node.next = prev.next
        prev.next = new_node
        
        # Increment size
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if valid.
        :type index: int
        :rtype: None
        """
        # Validate index
        if index < 0 or index >= self.size:
            return
        
        # Traverse to the (index-1)-th node
        prev = self.head
        for i in range(index):
            prev = prev.next
        
        # Delete the index-th node
        prev.next = prev.next.next
        
        # Decrement size
        self.size -= 1

# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    # Example 1
    print("=== Example 1 ===")
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
    print(f"get(1): {myLinkedList.get(1)}")  # return 2
    myLinkedList.deleteAtIndex(1)  # now the linked list is 1->3
    print(f"get(1): {myLinkedList.get(1)}")  # return 3
    
    # Example 2
    print("\n=== Example 2 ===")
    myLinkedList2 = MyLinkedList()
    myLinkedList2.addAtHead(7)
    myLinkedList2.addAtHead(2)
    myLinkedList2.addAtHead(1)
    myLinkedList2.addAtIndex(3, 0)  # linked list becomes 1->2->7->0
    myLinkedList2.deleteAtIndex(2)  # linked list becomes 1->2->0
    myLinkedList2.addAtHead(6)  # linked list becomes 6->1->2->0
    myLinkedList2.addAtTail(4)  # linked list becomes 6->1->2->0->4
    print(f"get(4): {myLinkedList2.get(4)}")  # return 4
    myLinkedList2.addAtHead(4)  # linked list becomes 4->6->1->2->0->4
    myLinkedList2.addAtIndex(5, 0)  # linked list becomes 4->6->1->2->0->0->4
    myLinkedList2.addAtHead(6)  # linked list becomes 6->4->6->1->2->0->0->4
    
    # Example 3 - Edge cases
    print("\n=== Example 3 - Edge Cases ===")
    myLinkedList3 = MyLinkedList()
    print(f"get(0) on empty list: {myLinkedList3.get(0)}")  # return -1
    myLinkedList3.addAtIndex(0, 10)  # linked list becomes 10
    print(f"get(0): {myLinkedList3.get(0)}")  # return 10
    myLinkedList3.deleteAtIndex(0)  # linked list becomes empty
    print(f"get(0) after delete: {myLinkedList3.get(0)}")  # return -1