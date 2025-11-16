"""
===========================================================
287. Find the Duplicate Number (Floyd’s Cycle Detection)
===========================================================

🧩 Problem:
Given an array nums of length n+1 with numbers in the range [1, n],
exactly one number appears more than once. Return that number.

You must not modify the array and must use O(1) extra space.

-----------------------------------------------------------
Approach — Fast & Slow (Cycle Detection):
-----------------------------------------------------------
Treat the array as a linked list:

index → nums[index] → next index

Because a number repeats, it forms a cycle.
The duplicate number is the cycle's entry point.

Use Floyd’s cycle detection:
1. Move slow = nums[slow]
2. Move fast = nums[nums[fast]]
3. When they meet, reset slow to nums[0]
4. Move both 1 step until they meet again → duplicate number.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""

class Solution(object):
    def findDuplicate(self, nums):
        # Phase 1: Detect cycle
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find cycle entrance
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
