"""
===========================================================
503. Next Greater Element II
===========================================================

🧩 Problem:
You are given a **circular array** `nums` (i.e., the end connects back to the start).

For each element `nums[i]`, you need to find:
    ➜ The next greater element when moving to the right,
       **wrapping around** to the beginning if needed.

If no such element exists, return -1 for that position.

🎯 Goal:
Return an array `answer` where:
    answer[i] = next greater element of nums[i] in the circular array,
    or -1 if it does not exist.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  nums = [1, 2, 1]

Circular view:
    Index:   0   1   2
    Value:   1   2   1
    Wrap:   [1, 2, 1, 1, 2, 1] (conceptually)

For each index:
    i = 0, val = 1 → next greater = 2 (at index 1)
    i = 1, val = 2 → no greater in circular traversal → -1
    i = 2, val = 1 → next greater = 2 (wraps to index 1)

Output: [2, -1, 2]


Example 2:
Input:  nums = [3, 8, 4, 1, 2]
Possible answers:
    3 → 8
    8 → -1   (no greater element in circular array)
    4 → -1
    1 → 2
    2 → 3    (wrap-around)
Output: [8, -1, -1, 2, 3]

-----------------------------------------------------------
Key Idea — Circular "Next Greater" with Monotonic Stack:
-----------------------------------------------------------

Pattern: 🧱 Monotonic Decreasing Stack — Next Greater Element (Circular)

For the normal (non-circular) next greater element:
    - We process from right to left.
    - Maintain a stack of values that are "candidates" for next greater.
    - While top of stack <= current value → pop (not useful).
    - After popping smaller/equal ones:
         - If stack not empty → its top is the next greater.
         - Else → no greater element (answer = -1).

For the **circular** case:
    - We need to "see" elements to the right and also those at the beginning.
    - Trick: iterate the array **twice** (2 * n - 1 down to 0).
    - Use index `i % n` to wrap around.
    - Only fill result when `i < n` (first pass from right to left).

Steps:
1. Let n = len(nums), result = [-1] * n
2. Use a stack to store **indices** of elements in a **monotonic decreasing fashion**
   based on their values.
3. Iterate i from 2n-1 down to 0:
       real_i = i % n
       current_val = nums[real_i]

       While stack not empty AND nums[stack[-1]] <= current_val:
            pop stack
       If i < n:
            If stack not empty → result[real_i] = nums[stack[-1]]
            Else → result[real_i] = -1
       Push real_i onto stack.
4. Return result.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n)
    - We iterate 2n steps, each index is pushed/popped at most once.

Space Complexity:  O(n)
    - Stack stores indices; result array also size n.

-----------------------------------------------------------
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        Finds the next greater element for each element in a circular array.

        For each index i, we search to the right (and wrap around) to find
        the first element greater than nums[i]. If none exists, result[i] = -1.

        Uses a monotonic decreasing stack of indices and a double pass over
        the array to simulate circular behavior.

        Args:
            nums (List[int]): Circular array of integers.

        Returns:
            List[int]: List of next greater elements for each index.

        Example:
            >>> Solution().nextGreaterElements([1,2,1])
            [2, -1, 2]
        """
        n = len(nums)
        result = [-1] * n
        stack = []  # will store indices, maintaining a decreasing stack by value

        # Iterate from 2n - 1 down to 0 to simulate circular array
        for i in range(2 * n - 1, -1, -1):
            real_i = i % n
            current_val = nums[real_i]

            # Pop all values that are <= current value
            # Since they can't be "next greater" for current or any earlier index
            while stack and nums[stack[-1]] <= current_val:
                stack.pop()

            # Only fill the result during the "first pass" (i < n)
            if i < n:
                if stack:
                    result[real_i] = nums[stack[-1]]
                else:
                    result[real_i] = -1

            # Push current index as a candidate for next greater for previous elements
            stack.append(real_i)

        return result


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElements([1, 2, 1]))          # Expected: [2, -1, 2]
    print(sol.nextGreaterElements([3, 8, 4, 1, 2]))    # Example: [8, -1, -1, 2, 3]
    print(sol.nextGreaterElements([5, 4, 3, 2, 1]))    # Expected: [-1, 5, 5, 5, 5]
