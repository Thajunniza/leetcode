
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
321. Create Maximum Number

🧩 Problem:
Given two arrays of digits nums1 and nums2 and an integer k, create the largest possible
sequence of length k by picking digits from both arrays while preserving the relative order
of digits within each array.

You may pick any number of digits from each array as long as the total length is k.

🎯 Goal:
Return the lexicographically largest sequence (as a list of ints) of length k that can be
formed by merging subsequences from nums1 and nums2 while preserving internal order.

---

## Examples:

Example 1:
Input:
  nums1 = [3, 4, 6, 5]
  nums2 = [9, 1, 2, 5, 8, 3]
  k = 5
Output:
  [9, 8, 6, 5, 3]

Example 2:
Input:
  nums1 = [6, 7]
  nums2 = [6, 0, 4]
  k = 5
Output:
  [6, 7, 6, 0, 4]

Example 3:
Input:
  nums1 = [6, 5]
  nums2 = [6, 4]
  k = 3
Output:
  [6, 6, 5]

---

## Algorithm — Try all splits + Pick Max Subsequence + Greedy Merge:

1) **Pick Max Subsequence (Monotonic Stack):**
   For an array `arr` and desired length `t`, keep a decreasing stack:
   - While we can drop elements (`drop = len(arr) - t`) and the top of the stack is less than
     the current element, pop the stack to let larger digits come earlier.
   - Push the current element.
   - At the end, return the first `t` elements of the stack.

2) **Try all valid splits of k:**
   - Let `take1` be the number of digits we take from `nums1`.
   - `take1` must be in `[max(0, k - len(nums2)), min(len(nums1), k)]`.
   - For each `take1`:
       * `part1 = pick_max_subsequence(nums1, take1)`
       * `part2 = pick_max_subsequence(nums2, k - take1)`
       * `candidate = merge(part1, part2)`
       * Keep the maximum candidate (lexicographically).

3) **Greedy Merge by Suffix Comparison:**
   - Maintain pointers `i, j` for `part1, part2`.
   - At each step, compare the **remaining suffixes** `part1[i:]` vs `part2[j:]` lexicographically.
   - Pick from the side whose **remaining suffix** is larger.
   - This resolves ties correctly when the next digits are equal.

---

⏱ Time Complexity (typical):
- Picking max subsequence: O(n) per array per attempt.
- Merging: O(k) steps, with suffix comparisons that can walk forward on ties.
- Trying all splits: up to O(k) attempts.
Overall practical complexity ≈ O(k * (|nums1| + |nums2|)), with efficient merging.

💾 Space Complexity:
- O(k) for the result and O(n) for temporary stacks (bounded by input sizes).

---

"""

# ------------------------------------
# Create Maximum Number — Implementation
# ------------------------------------

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def get_max_Seq(arr, seqLen):
            """
            Pick the lexicographically largest subsequence of exact length seqLen
            using a monotonic decreasing stack (greedy).
            """
            if seqLen == 0:
                return []
            drop = len(arr) - seqLen
            stack = []
            for x in arr:
                while drop > 0 and stack and stack[-1] < x:
                    stack.pop()
                    drop -= 1
                stack.append(x)
            return stack[:seqLen]  # ensure exact length

        def greater_suffix(a, i, b, j):
            """
            Return True iff the suffix a[i:] is lexicographically greater than b[j:],
            comparing without creating slice objects.
            """
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1
            if j == len(b):
                return True   # b exhausted ⇒ a's remainder is >= b's
            if i == len(a):
                return False  # a exhausted ⇒ b's remainder is greater
            return a[i] > b[j]  # first differing digit decides

        def mergeSeq(arr1, arr2):
            """
            Greedily merge two subsequences into the lexicographically largest sequence
            by choosing from the side whose remaining suffix is larger.
            """
            i = j = 0
            merged = []
            while i < len(arr1) or j < len(arr2):
                if j == len(arr2) or (i < len(arr1) and greater_suffix(arr1, i, arr2, j)):
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1
            return merged

        # Compute valid range of digits to take from nums1
        l1, l2 = len(nums1), len(nums2)
        min_take1 = max(0, k - l2)
        max_take1 = min(l1, k)

        best = []
        for take1 in range(min_take1, max_take1 + 1):  # inclusive
            part1 = get_max_Seq(nums1, take1)
            part2 = get_max_Seq(nums2, k - take1)
            candidate = mergeSeq(part1, part2)
            if candidate > best:
                best = candidate
        return best


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
    # Expected: [9, 8, 6, 5, 3]

    # Example 2
    print(sol.maxNumber([6, 7], [6, 0, 4], 5))
    # Expected: [6, 7, 6, 0, 4]

    # Additional edge tests
    print(sol.maxNumber([6, 5], [6, 4], 3))
    # Expected: [6, 6, 5]  (equal first digit; suffix on nums1 wins)

    print(sol.maxNumber([0, 0, 0], [0, 0], 4))
    # Expected: [0, 0, 0, 0]

    print(sol.maxNumber([], [1, 2, 3], 2))
    # Expected: [2, 3]

    print(sol.maxNumber([1, 2, 3], [], 2))
    # Expected: [2, 3]
