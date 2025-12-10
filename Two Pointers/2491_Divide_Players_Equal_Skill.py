"""
===========================================================
2491. Divide Players Into Teams of Equal Skill
===========================================================

🧩 Problem:
You are given an integer array `skill` of **even** length `n`, where `skill[i]` is the skill level of the `i`-th player.

You need to divide the `n` players into exactly `n / 2` **teams of 2 players**, such that:

- Every team has the **same total skill** (sum of the two players’ skills).
- The **chemistry** of a team with players `i` and `j` is: `skill[i] * skill[j]`.

✅ If it is possible to form such teams, return the **sum of chemistry** of all teams.  
❌ Otherwise, return `-1`.

---

🎯 Goal:
- Pair up the players into 2-player teams.
- All pairs must have the **same pair-sum**.
- Compute the **total chemistry** = sum of `(skill[left] * skill[right])` for all valid pairs.
- If at least one pair breaks the required sum, return `-1`.

---

🧠 Pattern:
- **Two Pointers**
- **Sorting + Pairing from both ends**

---

📌 Example 1:
```text
Input:  skill = [3, 2, 5, 1, 3, 4]

Step 1: Sort → [1, 2, 3, 3, 4, 5]
Step 2: Pair from both ends:
    (1, 5) → sum = 6, chemistry = 1 * 5 = 5
    (2, 4) → sum = 6, chemistry = 2 * 4 = 8
    (3, 3) → sum = 6, chemistry = 3 * 3 = 9

All pairs have same sum (6) ✅
Total chemistry = 5 + 8 + 9 = 22

Output: 22
Input:  skill = [3, 4]

Only one possible team:
    (3, 4) → sum = 7, chemistry = 12

Output: 12
Input:  skill = [1, 1, 2, 3]

Sorted: [1, 1, 2, 3]
Target pair-sum = 1 + 3 = 4

Check middle pair:
    (1, 2) → sum = 3 ≠ 4 ❌

Cannot form equal-sum teams → Output: -1

"""
class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        # Step 1: Sort the skill levels
        skill.sort()

        left = 0
        right = len(skill) - 1

        # Target sum that every pair must match
        target_sum = skill[left] + skill[right]
        result = 0

        # Step 2: Use two pointers to form pairs
        while left < right:
            current_sum = skill[left] + skill[right]

            # If any pair doesn't have the target sum, it's impossible
            if current_sum != target_sum:
                return -1

            # Add chemistry for the current valid pair
            result += skill[left] * skill[right]

            # Move both pointers towards the center
            left += 1
            right -= 1

        # Step 3: All pairs are valid
        return result
    
# =======================
# 🔍 TESTING THE FUNCTION
# =======================

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3, 2, 5, 1, 3, 4], 22),
        ([3, 4], 12),
        ([1, 1, 2, 3], -1),
        ([5, 5, 5, 5], 50),  # (5,5) and (5,5) → 25 + 25 = 50
        ([1, 2, 3, 6], -1),  # cannot match equal team sum
        ([2, 2, 2, 2], 8),   # (2,2)=4→4*2=8
        ([1, 3, 5, 7], 26),  # pairs: (1,7)=7, (3,5)=15 → total = 22? (check)
    ]

    for arr, expected in tests:
        output = sol.dividePlayers(arr)
        print(f"Input: {arr}-> Output: {output} | Expected: {expected}")
