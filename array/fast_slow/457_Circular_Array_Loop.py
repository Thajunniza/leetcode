"""
===========================================================
457. Circular Array Loop
===========================================================

🧩 Problem:
You are given a circular integer array nums of length n.

A "move" from index i is defined as:
    next_index = (i + nums[i]) % n

You must determine whether the array contains a loop that satisfies ALL of these:

1. The loop length is greater than 1 (no single-element loop).
2. The loop moves in only ONE direction:
       - Either all numbers in the loop are positive (forward)
       - Or all numbers in the loop are negative (backward)

Return True if such a loop exists, otherwise return False.

🎯 Goal:
Detect if there exists a valid "cycle" in this circular array, obeying the direction
and length constraints, using O(n) time and O(1) extra space.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [2, -1, 1, 2, 2]
Output: True

Explanation:
    From index 0:
    - 0 → (0 + 2) % 5 = 2
    - 2 → (2 + 1) % 5 = 3
    - 3 → (3 + 2) % 5 = 0
    All moves are positive and form a loop of length 3.

Example 2:
Input:  nums = [-1, 2]
Output: False

Explanation:
    - From index 0: only moves backward.
    - From index 1: only moves forward.
    No valid loop that keeps a single direction and length > 1.

Example 3:
Input:  nums = [-1, -2, -3, -4, -5, 6]
Output: False

Explanation:
    The element 6 jumps into the segment of negative numbers, breaking the
    single-direction rule. No valid loop exists.

Example 4:
Input: nums = [1, 1, 1, 1, 1]
Output: True

Explanation:
    Every move is forward and you can loop around the entire array.

-----------------------------------------------------------
Algorithm — Fast & Slow Pointers on Array:
-----------------------------------------------------------

Core idea:
    Similar to detecting a cycle in a linked list (Floyd’s Tortoise & Hare),
    but here the "next node" is computed using array indices:

        next_index = (i + nums[i]) % n

We must also enforce:
    - Single direction (all +ve or all -ve)
    - Loop length > 1

Steps:

1. Define a helper getNextIndex(curr, direction):
       - If nums[curr] is 0 → this index is already processed → return -1.
       - Check if nums[curr] has the same sign as `direction`. If not → return -1.
       - Compute nxt = (curr + nums[curr]) % n.
       - If nxt == curr → single-element loop → invalid → return -1.
       - Check if nums[nxt] has the same sign as `direction`. If not → return -1.
       - If nums[nxt] is 0 → next is processed/invalid → return -1.
       - Otherwise return nxt.

2. For each index i in [0 .. n-1]:
       - If nums[i] == 0 → skip (this path is already evaluated earlier).
       - Set direction = (nums[i] > 0)  # True for forward, False for backward.
       - Initialize:
             slow = i
             fast = i

3. Use fast & slow pointers:
       While True:
           - Move slow by 1 step: slow = getNextIndex(slow, direction)
                 If slow == -1 → break this loop (no valid cycle from this start).
           - Move fast by 2 steps:
                 fast = getNextIndex(fast, direction)
                 If fast == -1 → break
                 fast = getNextIndex(fast, direction)
                 If fast == -1 → break
           - If slow == fast → cycle found → return True.

4. If we exit the while-loop without finding a cycle:
       - We know the path starting from i is invalid.
       - To avoid re-checking this path from other starting points,
         we "mark" every index in this path as visited by setting nums[j] = 0.
       - Do:
             j = i
             while nums[j] != 0 and (nums[j] > 0) == direction:
                 nxt = (j + nums[j]) % n    # raw next index in circular array
                 nums[j] = 0                # mark current index as processed
                 j = nxt

5. After checking all i:
       - If no valid cycle was found, return False.

-----------------------------------------------------------
⏱ Time Complexity:
- Each element is visited at most a constant number of times.
- Due to marking visited paths (setting nums[j] = 0), we never repeatedly
  traverse the same path.
- Overall: O(n)

💾 Space Complexity:
- Only uses a few variables (slow, fast, indices, booleans).
- Modifies nums in-place for marking.
- Extra space: O(1)

-----------------------------------------------------------
 
"""

# ------------------------------------
# 457. Circular Array Loop — Fast & Slow Pointers on Array
# ------------------------------------
from typing import List


def circular_array_loop(nums: List[int]) -> bool:
    """
    Determine if the circular array contains a valid loop.

    A valid loop must:
        - Have length > 1 (no single-element loops)
        - Move in only one direction:
              * all positive (forward) OR
              * all negative (backward)

    Args:
        nums (List[int]): The circular array of integers.

    Returns:
        bool: True if there exists a valid loop, otherwise False.

    Example:
        >>> circular_array_loop([2, -1, 1, 2, 2])
        True
        >>> circular_array_loop([-1, 2])
        False
    """

    arr_len = len(nums)

    def get_next_index(curr: int, direction: bool) -> int:
        """
        Get the next index in the circular array from 'curr'
        while enforcing direction and validity rules.

        Returns:
            - next index if move is valid
            - -1 if the move is invalid:
                  * direction mismatch
                  * single-element loop
                  * already processed (nums[index] == 0)
        """
        # If already processed, this index is not part of any valid loop
        if nums[curr] == 0:
            return -1

        # Current element must follow the initial direction
        if (nums[curr] > 0) != direction:
            return -1

        nxt = (curr + nums[curr]) % arr_len

        # Single-element loop is not allowed
        if nxt == curr:
            return -1

        # Next element must also follow the same direction
        if (nums[nxt] > 0) != direction:
            return -1

        # If next is already processed, no valid loop through it
        if nums[nxt] == 0:
            return -1

        return nxt

    for i in range(arr_len):
        # Skip if this index was already marked as visited/invalid
        if nums[i] == 0:
            continue

        # True for forward (positive), False for backward (negative)
        direction = nums[i] > 0

        slow = i
        fast = i

        # Try to detect a cycle starting from index i
        while True:
            slow = get_next_index(slow, direction)
            if slow == -1:
                break

            fast = get_next_index(fast, direction)
            if fast == -1:
                break
            fast = get_next_index(fast, direction)
            if fast == -1:
                break

            # Cycle detected
            if slow == fast:
                return True

        # 🧹 No valid loop from this starting index
        # Mark the entire path as visited so we don't re-check it later
        j = i
        while nums[j] != 0 and (nums[j] > 0) == direction:
            nxt = (j + nums[j]) % arr_len  # raw circular move
            nums[j] = 0                    # mark current index as processed
            j = nxt

    # No valid cycle found in the entire array
    return False


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    print(circular_array_loop([2, -1, 1, 2, 2]))       # True
    print(circular_array_loop([-1, 2]))                # False
    print(circular_array_loop([-1, -2, -3, -4, -5]))   # True (full negative loop)
    print(circular_array_loop([-1, -2, -3, -4, -5, 6]))# False
    print(circular_array_loop([1, 1, 1, 1, 1]))        # True
