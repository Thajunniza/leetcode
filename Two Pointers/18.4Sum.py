"""

18. 4Sum

🧩 Problem:
Given an integer array nums and an integer target, return all the UNIQUE
quadruplets [nums[i], nums[j], nums[k], nums[l]] such that:

```
i != j, i != k, i != l
j != k, j != l
k != l
nums[i] + nums[j] + nums[k] + nums[l] == target
```

The solution set must not contain duplicate quadruplets.

🎯 Goal:
Find all unique combinations of 4 numbers in the array that sum to target.

---

## Examples:

Example 1:
Input:  nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
Explanation:
Valid quadruplets that sum to 0:
- [-2, -1, 1, 2]  → 0
- [-2,  0, 0, 2]  → 0
- [-1,  0, 0, 1]  → 0
No duplicates allowed.

Example 2:
Input:  nums = [2, 2, 2, 2, 2], target = 8
Output: [[2, 2, 2, 2]]
Explanation:
Only one unique quadruplet.

Example 3:
Input:  nums = [0, 0, 0, 0], target = 1
Output: []
Explanation:
No quadruplet can sum to 1.

---

## Algorithm — Sorting + Two Pointers (inside 2 loops):

1. Sort the array nums.

2. Loop i from 0 to n-4:
   - If i > 0 and nums[i] == nums[i-1], skip i (avoid duplicates).

3. Loop j from i+1 to n-3:
   - If j > i+1 and nums[j] == nums[j-1], skip j (avoid duplicates).

4. For each (i, j), use TWO POINTERS:
   left  = j + 1
   right = n - 1

   While left < right:
   total = nums[i] + nums[j] + nums[left] + nums[right]

   ```
   - If total == target:
         → Add quadruplet to result.
         → Skip duplicates for left (move while same).
         → Skip duplicates for right (move while same).
         → Move both inward.

   - If total < target:
         → Need a larger sum → left += 1

   - If total > target:
         → Need a smaller sum → right -= 1
   ```

5. Return the list of unique quadruplets.

---

⏱ Time Complexity:

* Sorting: O(n log n)
* Two loops (i, j) + two-pointer scan: O(n^3) worst case
* Total: O(n^3)

💾 Space Complexity:

* O(1) extra (ignoring output), since sorting can be in-place
* Output uses O(k) for k quadruplets

---

"""

# ------------------------------------

# 4Sum — Sorting + Two Pointers

# ------------------------------------

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = n -1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums [r]
                    if total == target:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return result
        

# ------------------------------------

# Driver Test

# ------------------------------------

s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
# Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

print(s.fourSum([2, 2, 2, 2, 2], 8))
# Expected: [[2, 2, 2, 2]]

print(s.fourSum([0, 0, 0, 0], 1))
# Expected: []

