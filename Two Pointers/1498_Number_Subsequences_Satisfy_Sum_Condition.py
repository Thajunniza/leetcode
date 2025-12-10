"""
===========================================================
1498. Number of Subsequences That Satisfy the Given Sum Condition
===========================================================

🧩 Problem:
You are given an integer array `nums` and an integer `target`.

A **subsequence** is any sequence you take by selecting elements in order (not necessarily contiguous).

Your task is to count the number of **non-empty subsequences** such that:

min(subsequence) + max(subsequence) ≤ target


Return the answer **modulo 10⁹ + 7**.

---

🎯 Goal:
Count how many subsequences satisfy:

- smallest element = some `nums[l]`
- largest element = some `nums[r]`
- and `nums[l] + nums[r] ≤ target`

---

🧠 Key Insight (Very Important!):

After **sorting** the array:

nums = [a0, a1, a2, ..., an-1]


Use **two pointers**:

- `l` → candidate minimum element  
- `r` → candidate maximum element  

If:

nums[l] + nums[r] ≤ target

Then **ALL** subsequences whose:

- min = nums[l]
- max = nums[r]  
- middle elements = **any combination** of elements between `l` and `r`

are valid.

The number of ways to choose any middle elements is:

2^(r - l)

(Either include or exclude each element between l and r.)

So we **add** `2^(r-l)` to result and move `l += 1`.

If:

nums[l] + nums[r] > target

Then `nums[r]` is too large to pair with nums[l]  
→ move `r -= 1`.

---

📌 Example:
nums = [3, 5, 6, 7], target = 9
Sorted: [3,5,6,7]
Valid subsequences:
[3], [3,5], [3,6], [3,5,6] → 4

---

🧮 Constraints:
- `1 ≤ nums.length ≤ 10⁵`
- `1 ≤ nums[i] ≤ 10⁶`
- `1 ≤ target ≤ 10⁶`
- Must return answer modulo `10⁹ + 7`

---

💡 Why Sorting + Two Pointers Works

Because after sorting:

- Every subsequence’s minimum = nums[l]
- Every subsequence’s maximum = nums[r]
- Middle elements can be chosen freely, since they are always ≥ nums[l] and ≤ nums[r]

This gives a clean two-pointer structure.

---

🧾 Algorithm:
1. **Sort** `nums`.
2. Precompute powers of 2 OR use `pow(2, x, mod)` safely.
3. Initialize:
l = 0
r = len(nums) - 1
result = 0
4. While `l ≤ r`:
- If `nums[l] + nums[r] ≤ target`:
  - Add `2^(r - l)` subsequences.
  - Move `l += 1`
- Else:
  - Move `r -= 1`
5. Return `result % mod`.

---

⏱️ Time & Space Complexity:
- Sorting → `O(n log n)`
- Two pointers → `O(n)`
- Total → `O(n log n)`
- Space → `O(1)` extra (or `O(n)` if precomputing powers)

---

💻 Python Solution (Your Correct Version + Small Cleanup)

```python
"""
class Solution(object):
 def numSubseq(self, nums, target):
     """
     :type nums: List[int]
     :type target: int
     :rtype: int
     """
     nums.sort()
     mod = 10 ** 9 + 7
     n = len(nums)
     l = 0
     r = n - 1
     result = 0

     while l <= r:
         if nums[l] + nums[r] <= target:
             # Count all subsequences where nums[l] is min and nums[r] is max
             result = (result + pow(2, r - l, mod)) % mod
             l += 1
         else:
             r -= 1

     return result

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3,5,6,7], 9, 4),
        ([3,3,6,8], 10, 6),
        ([2,3,3,4,6,7], 12, 61),
        ([5,2,4,1,7,6,8], 16, 127),
        ([1], 1, 1),
        ([1], 2, 1),
        ([2,9,6,8,2], 10, 6),
    ]

    for nums, target, expected in tests:
        output = sol.numSubseq(nums[:], target)
        print(f"nums={nums}, target={target} -> Output: {output} | Expected: {expected}")

