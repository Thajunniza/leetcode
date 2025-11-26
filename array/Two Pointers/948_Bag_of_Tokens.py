"""
===========================================================
948. Bag of Tokens
===========================================================

🧩 Problem:
You are given:
- An integer array `tokens` representing token values.
- An integer `power` representing your initial power.

Rules:
- You can play tokens in two ways:
    1. **Face up**: Spend `tokens[i]` power → gain 1 score.
    2. **Face down**: Spend 1 score → gain `tokens[i]` power.
- Each token can be used at most once.
- You can play tokens in any order.

Your task:
- Return the **maximum score** you can achieve.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    tokens = [100,200,300,400], power = 200

Process:
    - Sort tokens: [100,200,300,400]
    - Play 100 face up → power = 100, score = 1
    - Play 200 face up → power = -100 (not possible)
    - Instead, sell 400 face down → power = 500, score = 0
    - Play 200 face up → power = 300, score = 1
    - Play 300 face up → power = 0, score = 2

Output:
    2

Example 2:
Input:
    tokens = [100], power = 50
Output:
    0

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

Maximize score by:
- Spending smallest tokens for score.
- Selling largest tokens for power when needed.

Pattern / Folder:
    • Pattern: Greedy + Two Pointers
    • Folder suggestion:
        /Greedy/948-BagOfTokens/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

Greedy idea:
- Sort tokens.
- Use two pointers:
    - `l` → smallest token
    - `r` → largest token
- While possible:
    - If we have enough power for `tokens[l]`:
        - Play face up → gain score
    - Else if we have score > 0:
        - Sell largest token → regain power
    - Else:
        - Stop (cannot proceed further)

-----------------------------------------------------------
🧠 Algorithm (Greedy + Two Pointers):
-----------------------------------------------------------

1. Sort tokens.
2. Initialize:
       l = 0
       r = len(tokens) - 1
       score = 0
       max_score = 0
3. While l ≤ r:
       if tokens[l] ≤ power:
           power -= tokens[l]
           score += 1
           max_score = max(max_score, score)
           l += 1
       elif score > 0:
           power += tokens[r]
           score -= 1
           r -= 1
       else:
           break
4. Return max_score.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time Complexity:
    • Sorting: O(n log n)
    • Two-pointer scan: O(n)
  Overall: O(n log n)

- Space Complexity:
    • O(1) extra

-----------------------------------------------------------
✅ Python Solution:
-----------------------------------------------------------
"""
class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        """
        LeetCode 948. Bag of Tokens
        Greedy + Two-pointer solution.

        Args:
            tokens (List[int]): token values
            power (int): initial power

        Returns:
            int: maximum score achievable
        """
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        max_score = 0

        while l <= r:
            if tokens[l] <= power:
                # Play token face up: spend power, gain score
                power -= tokens[l]
                score += 1
                max_score = max(max_score, score)
                l += 1
            elif score > 0:
                # Play token face down: regain power, lose score
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return max_score


# ▶️ TEST CASES
if __name__ == "__main__":
    S = Solution()

    tokens1 = [100,200,300,400]
    power1 = 200
    print(S.bagOfTokensScore(tokens1, power1))  # Expected: 2

    tokens2 = [100]
    power2 = 50
    print(S.bagOfTokensScore(tokens2, power2))  # Expected: 0
