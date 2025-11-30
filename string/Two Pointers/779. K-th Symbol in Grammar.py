"""
===========================================================
779. K-th Symbol in Grammar
===========================================================

🧩 Problem:
We start with a single row: "0".  
Every next row is constructed by replacing:
    • 0 → "01"
    • 1 → "10"

Given two integers **n** (row number) and **k** (1-indexed position)**,  
return the **k-th symbol** in the n-th row.

🎯 Goal:
Find the symbol (0 or 1) at position k in the n-th row of the grammar sequence.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  n = 1, k = 1  
Output: 0  
Explanation: Row 1 = "0"

Example 2:
Input:  n = 2, k = 1  
Output: 0  
Explanation: Row 2 = "01"

Example 3:
Input:  n = 2, k = 2  
Output: 1  
Explanation: Row 2 = "01"

Example 4:
Input:  n = 4, k = 5  
Output: 1  
Explanation:
    Row 1: 0  
    Row 2: 01  
    Row 3: 0110  
    Row 4: 01101001  
    5th symbol = 1

-----------------------------------------------------------
🧠 Intuition:
-----------------------------------------------------------
Instead of generating the whole row (which becomes huge),
we observe:

Each row is formed by expanding previous row:
- First half = previous row  
- Second half = flipped previous row  

So:
• If k is in **first half**, answer = kth symbol of previous row  
• If k is in **second half**, answer = **flip** of (k - half)th symbol of previous row  

This gives a clean **recursive** solution.

-----------------------------------------------------------
✅ Algorithm:
-----------------------------------------------------------
1. Base Case:  
   If n == 1 → return 0

2. Find mid = 2^(n-1) / 2

3. If k ≤ mid  
       → return kth symbol of previous row  
   Else  
       → return flipped( (k - mid)th symbol of previous row )

4. Flip rule:  
       0 → 1  
       1 → 0

-----------------------------------------------------------
💡 Better Insight (Google-level):
-----------------------------------------------------------
This is actually counting how many times k-1 has **bit 1** in its binary form.  
Because every time you fall into second half, you flip.

So:
symbol = number_of_1s_in_binary(k-1) % 2
-----------------------------------------------------------
⏱️ Complexity:
-----------------------------------------------------------
Time:  O(n)  
Space: O(n)  (due to recursion)

===========================================================

-----------------------------------------------------------
💻 Code (Recursive)
-----------------------------------------------------------
"""
class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        
        mid = 2 ** (n - 1) // 2
        
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (1, 1, 0),   # Row 1: 0
        (2, 1, 0),   # Row 2: 0 1
        (2, 2, 1),
        (3, 1, 0),   # Row 3: 0 1 1 0
        (3, 2, 1),
        (3, 3, 1),
        (3, 4, 0),
        (4, 5, 1),   # Row 4: 0 1 1 0 1 0 0 1
        (4, 8, 1),
        (5, 16, 0),
    ]

    for n, k, expected in tests:
        output = sol.kthGrammar(n, k)
        print(f"n={n}, k={k} -> Output: {output} | Expected: {expected}")

