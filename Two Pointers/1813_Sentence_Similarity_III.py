
"""
===========================================================
1813. Sentence Similarity III
===========================================================

🧩 Problem:
Two sentences `sentence1` and `sentence2` are strings of words separated by spaces.

A sentence is **similar** to another sentence if you can insert some *words in the middle* of either sentence so that both become **exactly the same**.

✳️ Important:
Only **insertions** are allowed.  
Deletions are not allowed.  
Comparisons must match words **exactly**.

Return **True** if the two sentences are similar.

---

🎯 Goal:
Check if the **shorter sentence** is a subsequence of the longer sentence,  
*but only allowed as*:  
- A **prefix match**, or  
- A **suffix match**, or  
- A **combination of prefix + suffix**,  
with the unmatched part (if any) appearing **only in the longer sentence**.

Example:

`s1 = "I love coding"`  
`s2 = "I really love coding a lot"`

Prefix:    "I"  
Suffix:    "love coding"  
Everything matches → similar.

---

🧠 Pattern:
- **Two Pointers**
- Compare prefix words
- Compare suffix words
- Ensure shorter sentence is fully matched

---

📌 Example 1:
Input:
sentence1 = "My name is Haley"
sentence2 = "My Haley"

Output: True

Explanation:
Prefix: "My"
Suffix: "Haley"
Middle "name is" is OK since it appears only in the longer sentence.

📌 Example 2:
Input:
sentence1 = "of"
sentence2 = "A lot of words"

Output: True

📌 Example 3:
Input:
sentence1 = "Eating right now"
sentence2 = "Eating"

Output: False

---

🧮 Constraints:
- `1 <= sentence.length <= 100`
- Words contain lowercase or uppercase English letters
- Sentences may contain multiple spaces

---

💡 Intuition:

We only need to check if **all words of the shorter sentence** appear:
- starting from the left (prefix), and/or  
- starting from the right (suffix),  
without conflicting overlaps.

Procedure:
1. Split sentences into word arrays.
2. Ensure `s1` is **shorter**.
3. Move left pointers while words match.
4. Move right pointers while words match.
5. Final check:
   - If all words from `s1` are matched → `True`.

---

🧾 Algorithm:
1. Split both sentences into lists `s1` and `s2`.
2. If `len(s1) > len(s2)` → swap to ensure `s1` is shorter.
3. Initialize four pointers:
l1 = 0 r1 = len(s1) - 1
l2 = 0 r2 = len(s2) - 1
4. While left words match:
- Move `l1` and `l2` forward.
5. While right words match:
- Move `r1` and `r2` backward.
6. If all words of s1 are matched:
- `return l1 > r1`
7. Otherwise:
- `return False`.

---

⏱️ Time & Space Complexity:
- **Time:** O(n + m)
- **Space:** O(n + m)

---

💻 Python Solution (Your Correct Version):

```python
"""

class Solution(object):
 def areSentencesSimilar(self, sentence1, sentence2):
     """
     :type sentence1: str
     :type sentence2: str
     :rtype: bool
     """
     s1 = sentence1.split()
     s2 = sentence2.split()

     # Always make s1 the shorter sentence
     if len(s1) > len(s2):
         s1, s2 = s2, s1

     l1 = 0
     r1 = len(s1) - 1
     l2 = 0
     r2 = len(s2) - 1

     # Match prefix words
     while l1 <= r1 and s1[l1] == s2[l2]:
         l1 += 1
         l2 += 1

     # Match suffix words
     while l1 <= r1 and s1[r1] == s2[r2]:
         r1 -= 1
         r2 -= 1

     # All words in the shorter sentence must be matched
     return l1 > r1


