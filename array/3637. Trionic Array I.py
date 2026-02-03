"""
===========================================================
3637. Trionic Array I
===========================================================

🧩 Problem:
Given an array of **integers** `nums`, determine if it forms a **trionic pattern**:
- Starts with an **increase**
- Followed by a **decrease**
- Ends with a **second increase**

The **first and last elements must be included** in the pattern.  
Strictly increasing or decreasing sequences (no equal consecutive numbers) are required.

🎯 Goal:
Return **True** if the array forms a trionic pattern, otherwise **False**.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input: nums = [1, 3, 5, 4, 2, 6]
Output: True
Explanation: Pattern: 1→3→5 (increase), 5→4→2 (decrease), 2→6 (second increase)

Example 2:
Input: nums = [4, 1, 5, 2, 3]
Output: True
Explanation: Pattern: 4→1 (decrease starts after first increase?), first element included, last element included.

Example 3:
Input: nums = [1, 2, 3]
Output: False
Explanation: No decrease occurs, so no trionic pattern.

Example 4:
Input: nums = [3, 2, 1]
Output: False
Explanation: No initial increase, fails pattern.

-----------------------------------------------------------
Algorithm — State Machine:
-----------------------------------------------------------

Track the **phase of the pattern** with a single `state` variable:

1. Initialize `state = 0`:
   - 0: waiting for first increase from the first element
   - 1: after first increase, waiting for decrease
   - 2: after decrease, waiting for second increase
   - 3: second increase phase completed

2. Iterate through array from index 1 to n-1:
   - If current == previous → return False (strictly monotone required)
   - Phase 0: first increase from start
       → if increase, move to state 1
       → else return False
   - Phase 1: waiting for decrease
       → if decrease, move to state 2
       → else stay (still increasing)
   - Phase 2: waiting for second increase
       → if increase, move to state 3
       → else stay (still decreasing)
   - Phase 3: ensure no decrease occurs
       → if decrease, return False

3. Return True if `state == 3` at the end, else False

Key idea:
Use a **single state variable** to track the trionic phases,
allowing multiple consecutive increases or decreases within each phase.

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n)  
(Traverse array once)

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(1)  
(No extra data structures)

-----------------------------------------------------------
"""

# ------------------------------------
# Trionic Pattern Detection
# State Machine
# ------------------------------------

class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False

        state = 0  # 0: first increase, 1: decreasing, 2: second increase, 3: completed

        for i in range(1, n):
            a, b = nums[i-1], nums[i]

            if a == b:
                return False

            if state == 0:  # first increase from start
                if b > a:
                    state = 1
                else:
                    return False  # must start with increase
            elif state == 1:  # after first increase, waiting for decrease
                if b < a:
                    state = 2
                # else still increasing → stay in state 1
            elif state == 2:  # after decrease, waiting for second increase
                if b > a:
                    state = 3
                # else still decreasing → stay in state 2
            elif state == 3:  # ensure no decrease after second increase
                if b < a:
                    return False

        return state == 3

# ------------------------------------
# Driver Test
# ------------------------------------

sol = Solution()
print(sol.isTrionic([1,3,5,4,2,6]))  # Expected: True
print(sol.isTrionic([4,1,5,2,3]))    # Expected: True
print(sol.isTrionic([1,3,2,4]))      # Expected: True
print(sol.isTrionic([1,2,3]))        # Expected: False
print(sol.isTrionic([3,2,1]))        # Expected: False
print(sol.isTrionic([1,2,1,2]))      # Expected: True
print(sol.isTrionic([1,2,2,1,3]))    # Expected: False
print(sol.isTrionic([4,3,2,5,1,6]))  # Expected: False
