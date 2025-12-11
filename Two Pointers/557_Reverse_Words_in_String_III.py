""" 
===========================================================
557. Reverse Words in a String III
===========================================================

🧩 Problem:
Given a string `s`, reverse the **characters of each word** in the string,  
while preserving the **word order** and **spaces**.

A *word* is defined as a sequence of non-space characters.

-----------------------------------------------------------
🔍 Example:
-----------------------------------------------------------

Example 1:
Input:
    s = "Let's take LeetCode contest"

Process:
    "Let's"     → "s'teL"
    "take"      → "ekat"
    "LeetCode"  → "edoCteeL"
    "contest"   → "tsetnoc"

Output:
    "s'teL ekat edoCteeL tsetnoc"


Example 2:
Input:
    s = "God Ding"

Output:
    "doG gniD"

-----------------------------------------------------------
🎯 Goal:
-----------------------------------------------------------

For every word in the string:
- Reverse its characters
- Keep the words in the same order
- Preserve spaces exactly

Pattern / Folder:
    • Pattern: Two Pointers (String Manipulation)
    • Folder suggestion:
        /TwoPointers/557-ReverseWordsInStringIII/

-----------------------------------------------------------
💡 Intuition:
-----------------------------------------------------------

We need to reverse each word **individually** but not the entire string.

Approach:
1. Convert the string into a list of characters (optional)
2. Use two pointers:
    - `p` marks the start of a word
    - `q` moves until a space or end of string
3. When we reach a space or end:
    - Reverse the substring `s[p:q]`
    - Move `p` to start of next word

This method reverses each word in-place using only O(1) extra space.

Alternatively, a simpler Pythonic approach:
- Split → Reverse each → Join

-----------------------------------------------------------
🧠 Algorithm (Two Pointer – Reverse Each Word):
-----------------------------------------------------------

1. Convert string `s` into a list: `chars = list(s)`
2. Initialize:
       p = 0   # start of current word
3. Loop `i` from 0 to len(chars):
       If chars[i] == ' ':
           reverse chars[p:i-1]
           p = i + 1
4. After loop ends:
       reverse chars[p:len(chars)-1]  # reverse last word
5. Join and return `"".join(chars)`

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

Let:
- `n` = length of string

- Time Complexity: **O(n)**  
  Each character is visited a constant number of times.

- Space Complexity:  
  • Two-pointer in-place version: **O(1)**  
  • Pythonic split-based version: **O(n)**

-----------------------------------------------------------
✅ Python Solution (Two Pointers – Best for Interviews):
-----------------------------------------------------------
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        result = []
        for c in arr:
            result.append(c[::-1])
        return " ".join(result)
    
class Solution(object):
    def reverseWords(self, s):
        chars = list(s)
        n = len(chars)
        p = 0  # start of each word
        
        for i in range(n + 1):
            # End of word at i (space) or end of string
            if i == n or chars[i] == ' ':
                # Reverse chars[p:i-1]
                left, right = p, i - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                p = i + 1  # move to next word
        
        return "".join(chars)


# ▶️ TEST HERE
if __name__ == "__main__":
    S = Solution()
    print(S.reverseWords("Let's take LeetCode contest"))
    # Expected: "s'teL ekat edoCteeL tsetnoc"

    print(S.reverseWords("God Ding"))
    # Expected: "doG gniD"

