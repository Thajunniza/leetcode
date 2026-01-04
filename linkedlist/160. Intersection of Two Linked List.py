"""

160. Intersection of Two Linked Lists — Two-Pointer “Switch Heads”

🧩 Problem:
Given the heads of two singly linked lists `headA` and `headB`, return the **node** at which the two lists intersect.  
If the two linked lists have no intersection, return `None` (or `null`).

> Intersection means they share the **exact same node object** (same reference), not just equal values.

🎯 Goal:
Find the first shared node by reference where the two lists merge.

---

## Examples:

### Example 1 (Intersecting)
A: 1 → 2 → **7 → 8 → 9**  
B: 3 → 4 → 5 → **7 → 8 → 9**  
Output: Node with value `7`

### Example 2 (No Intersection)
A: 1 → 2 → 3  
B: 4 → 5  
Output: `None`

### Example 3 (Intersection at Head)
A: **10 → 11**  
B: **10 → 11**  
Output: Node with value `10`

---

## Algorithm — Two Pointers with Head Switching (Elegant, O(1) space)

1. Initialize two pointers:
   - `p` at `headA`
   - `q` at `headB`

2. Walk both pointers one step at a time:
   - If `p` reaches the end (`None`), **redirect** it to `headB`.
   - If `q` reaches the end (`None`), **redirect** it to `headA`.

3. Continue until `p == q`:
   - They either meet at the **intersection node**, or both become `None` (no intersection).

**Why it works:**  
After switching heads, both pointers traverse the same total length (`lenA + lenB`). This neutralizes any difference in initial lengths and guarantees a meeting point at the intersection node, or termination at `None` simultaneously if disjoint.

---

## Correctness Intuition (Short Sketch):

Let:
- `a` = unique prefix length of list A before intersection
- `b` = unique prefix length of list B before intersection
- `c` = shared tail length starting at the intersection

Pointer `p` traverses `a + c + b + c`. Pointer `q` traverses `b + c + a + c`.  
Both totals equal `a + b + 2c`, hence they align at the same node (the first shared node).  
If there is no shared tail (`c = 0`), both hit `None` after `lenA + lenB`.

---

## Edge Cases & Notes

- One or both lists empty → return `None`.
- Same values but different nodes → **not** an intersection.
- Intersection at the head → immediate return.
- Cycles are not considered in the standard problem; if cycles may exist, detect them first to avoid infinite loops.

---

## ⏱ Time & 💾 Space Complexity

- **Time:** `O(m + n)` — each pointer traverses at most two list lengths.
- **Space:** `O(1)` — constant extra space.

---

## Python — Your Solution (Cleaned + Typed)

```python
"""


def getIntersectionNode(headA, headB):
    p = headA
    q = headB
    # Traverse both lists; on reaching the end, switch heads.
    while p != q:
        p = p.next if p else headB
        q = q.next if q else headA
    return p

