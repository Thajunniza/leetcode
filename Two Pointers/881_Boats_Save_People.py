"""
===========================================================
881. Boats to Save People
===========================================================

🧩 Problem:
You are given an array `people` where `people[i]` is the **weight of the i-th person**, and an integer `limit` which is the **maximum weight each boat can carry**.

Each boat:
- Can carry **at most two people** at the same time.
- The **sum of weights** of the people on a boat must be **≤ limit**.

Return the **minimum number of boats** needed to carry everyone.

---

🎯 Goal:
Use **as few boats as possible** such that:
- Each boat has **1 or 2 people**.
- Total weight on each boat **≤ limit**.

---

🧠 Pattern:
- **Greedy**
- **Two Pointers** after sorting

---

📌 Example 1:
```text
Input:  people = [1, 2], limit = 3
Output: 1

Explanation:
- We can carry both (1, 2) together: 1 + 2 = 3 ≤ limit.
- Only 1 boat needed.
Input:  people = [3, 2, 2, 1], limit = 3
Output: 3

Explanation (after sorting → [1, 2, 2, 3]):
- Boat 1: (1, 2) → 3
- Boat 2: (2)    → 2
- Boat 3: (3)    → 3

Total boats = 3.
Input:  people = [3, 5, 3, 4], limit = 5
Output: 4

Explanation (after sorting → [3, 3, 4, 5]):
- Boat 1: (5)    → 5
- Boat 2: (4)    → 4
- Boat 3: (3)    → 3
- Boat 4: (3)    → 3

No two people can be paired without exceeding 5.
Total boats = 4.

"""

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # Sort people by weight
        people.sort()
        
        p = 0
        q = len(people) - 1
        boats = 0
        
        # Use two pointers: lightest (p), heaviest (q)
        while p <= q:
            # If the lightest + heaviest can share a boat, move p
            if people[p] + people[q] <= limit:
                p += 1
            
            # Heaviest person always goes in this boat
            q -= 1
            boats += 1
        
        return boats

# =======================
# 🔍 TESTING THE FUNCTION
# =======================

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # Basic examples
        (([1, 2], 3), 1),
        (([3, 2, 2, 1], 3), 3),
        (([3, 5, 3, 4], 5), 4),

        # Edge cases
        (([1], 3), 1),                           # Only one person
        (([2, 2], 3), 2),                         # Can't pair
        (([2, 2], 4), 1),                         # Can pair
        (([5, 5, 5], 5), 3),                      # All heavy, each alone
        (([1, 1, 1, 1], 2), 2),                   # All can pair

        # Mixed weights
        (([4, 2, 3, 1], 4), 3),
        (([2, 3, 4, 5], 5), 3),
        (([2, 3, 4, 5], 6), 2),

        # Larger values
        (([1, 2, 3, 4, 5, 6], 7), 3),             
        (([3, 8, 7, 1, 4], 9), 3),
    ]

    for (people, limit), expected in tests:
        output = sol.numRescueBoats(people[:], limit)   # [:] to avoid modifying original list
        print(f"people={people}, limit={limit} => Output: {output} | Expected: {expected}")
