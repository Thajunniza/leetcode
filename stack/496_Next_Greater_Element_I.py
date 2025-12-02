"""
===========================================================
496. Next Greater Element I
===========================================================

🧩 Problem:
You are given two integer arrays `nums1` and `nums2` where:

    • nums1 is a subset of nums2.
    • All elements in both arrays are unique.

For each element x in nums1, you need to find:
    ➜ The first greater element to the **right of x** in nums2.

If no such element exists, the answer for that element is -1.

🎯 Goal:
Return an array `answer` where:
    answer[i] = next greater element of nums1[i] in nums2,
    or -1 if it does not exist.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]

Process in nums2:
    1 → next greater is 3
    3 → next greater is 4
    4 → no greater → -1
    2 → no greater → -1

Mapping:
    1 → 3
    3 → 4
    4 → -1
    2 → -1

Answer for nums1:
    4 → -1
    1 →  3
    2 → -1
Output: [-1, 3, -1]


Example 2:
Input:
    nums1 = [2,4]
    nums2 = [1,2,3,4]

Process in nums2:
    1 → next greater is 2
    2 → next greater is 3
    3 → next greater is 4
    4 → -1

Mapping:
    1 → 2
    2 → 3
    3 → 4
    4 → -1

Answer for nums1:
    2 → 3
    4 → -1
Output: [3, -1]

-----------------------------------------------------------
Algorithm — Monotonic Stack (Decreasing):
-----------------------------------------------------------

Pattern: 🧱 Monotonic Stack — Next Greater Element (to the right)

Idea:
    • We only need to compute "next greater" in nums2 once.
    • Then answer queries for nums1 using a hashmap.

Steps:
1. Use a stack to process nums2 from left to right.
2. Maintain a **monotonic decreasing stack**:
       - While stack is not empty and current num > stack top:
             → current num is the "next greater element" for stack top.
             → pop top and store: next_greater[top] = current num
3. Push current num onto stack.
4. After processing all elements, any number left in stack has no greater element:
       → its next greater is -1.
5. Finally, for each x in nums1, lookup next_greater[x] (default -1).

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

Time Complexity:   O(n + m)
    - n = len(nums2), m = len(nums1)
    - Each element in nums2 is pushed and popped at most once.

Space Complexity:  O(n)
    - For the stack and the hashmap of next greater values.

-----------------------------------------------------------
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        Finds the next greater element for each number in nums1 based on nums2.

        For each element x in nums1, we look for the first greater element
        to the right of x in nums2. If it does not exist, return -1 for that x.

        Uses a monotonic decreasing stack to precompute next greater elements
        for all numbers in nums2.

        Args:
            nums1 (List[int]): Subset of nums2.
            nums2 (List[int]): Array containing all elements of nums1, in some order.

        Returns:
            List[int]: List of next greater elements corresponding to nums1.

        Example:
            >>> Solution().nextGreaterElement([4,1,2], [1,3,4,2])
            [-1, 3, -1]
        """
        next_greater = {}   # Map: number -> next greater number
        stack = []          # Monotonic decreasing stack (values from nums2)

        # Process nums2 to build next_greater map
        for num in nums2:
            # Current num is the "next greater" for all smaller stack tops
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num

            # Push current number to stack
            stack.append(num)

        # Remaining numbers in stack have no next greater element
        while stack:
            val = stack.pop()
            next_greater[val] = -1

        # Build result for nums1 using the precomputed map
        return [next_greater[num] for num in nums1]


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # Expected: [-1, 3, -1]
    print(sol.nextGreaterElement([2, 4], [1, 2, 3, 4]))     # Expected: [3, -1]
