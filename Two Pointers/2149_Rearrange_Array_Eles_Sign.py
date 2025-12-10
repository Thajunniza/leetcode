"""
===========================================================
2149. Rearrange Array Elements by Sign
===========================================================

🧩 Problem:
You are given a **0-indexed integer array `nums`** of even length containing an equal number
of **positive** and **negative** integers.

Your task is to rearrange the array so that:

- The **first element is positive**
- The **signs alternate** at each index
- The **relative order** of positive numbers is preserved
- The **relative order** of negative numbers is preserved

Return the rearranged array.

---

🎯 Goal:
Return an array that looks like:

[+, -, +, -, +, -, ...]


Where:
- Even indices   → **positive numbers**
- Odd indices    → **negative numbers**

Relative order must remain intact.

---

🧠 Pattern:
- **Two Pointers (index jump by 2)**
- **Stable ordering**
- **Extra array construction**

---

📌 Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Positives → placed at 0,2,4: [3,1,2]
Negatives → placed at 1,3,5: [-2,-5,-4]

📌 Example 2:
Input: nums = [-1,1]
Output: [1,-1]

---

🧮 Constraints:
- `2 <= nums.length <= 200000`
- nums.length is even
- #positives = #negatives
- `-10^5 <= nums[i] <= 10^5`

---

💡 Intuition:

Since the result must start with **positive**, we set:

- `p = 0` → pointer for next positive position  
- `q = 1` → pointer for next negative position  

Then iterate through `nums`:

- If the number is **positive** → place at `result[p]`, then `p += 2`
- If the number is **negative** → place at `result[q]`, then `q += 2`

This preserves the original order automatically, because we iterate through nums sequentially.

---

🧾 Algorithm:
1. Initialize result array of length n.
2. Set:
p = 0 # even index for positives
q = 1 # odd index for negatives
3. Loop through each number in nums:
- If positive → put at result[p]; p += 2  
- Else       → put at result[q]; q += 2  
4. Return result.

---

⏱️ Time & Space Complexity:
- **Time:** O(n)  
- **Space:** O(n) (required by problem)

---

💻 Python Solution (Your Version):

```python
"""
class Solution(object):
 def rearrangeArray(self, nums):
     """
     :type nums: List[int]
     :rtype: List[int]
     """
     p = 0                    # even index → positive
     q = 1                    # odd index → negative
     n = len(nums)
     result = [0] * n

     for x in nums:
         if x > 0:
             result[p] = x
             p += 2
         else:
             result[q] = x
             q += 2

     return result
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3,1,-2,-5,2,-4], [3,-2,1,-5,2,-4]),
        ([-1,1], [1,-1]),
        ([1,-1,2,-2,3,-3], [1,-1,2,-2,3,-3]),
        ([5,-3,4,-2,7,-1], [5,-3,4,-2,7,-1]),
        ([10,-5,20,-15], [10,-5,20,-15]),
    ]

    for nums, expected in tests:
        output = sol.rearrangeArray(nums[:])
        print(f"nums={nums} -> Output: {output} | Expected: {expected}")

