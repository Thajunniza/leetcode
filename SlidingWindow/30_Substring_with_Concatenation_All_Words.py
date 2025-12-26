"""
===========================================================
30. Substring with Concatenation of All Words
===========================================================

🧩 Problem:
Given a string `s` and an array of words `words`, return all starting
indices of substrings in `s` that are formed by **concatenating each word
in `words` exactly once**, **in any order**, and **without extra characters**.

All words in `words` have the same length.

🎯 Goal:
Find every index `i` such that:
    s[i : i + totalLength]  ==  a permutation (any order) of all words concatenated

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:  s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0, 9]
Explanation:
[0]  -> "barfoo"
[9]  -> "foobar"

Example 2:
Input:  s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
No combination uses both "word" twice.

Example 3:
Input:  s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6, 9, 12]

-----------------------------------------------------------
Algorithm — Sliding Window with Hash Frequency:
-----------------------------------------------------------

Let:
    wordLen  = length of each word
    wordCount = number of words
    totalLen = wordLen * wordCount

1. Build a frequency map `need` for all words in `words`.

2. For each offset `i` in range [0 ... wordLen - 1]:
       Use a sliding window where `left` and `right` move in word-by-word steps.
       Maintain a `seen` map counting words inside current window.

3. Expand:
       Extract substring = s[right:right + wordLen]
       If substring NOT in need:
             reset window, clear seen, move left to right+wordLen
       Else:
             add to seen
             While seen[word] > need[word]:
                   shrink window: decrease count at left,
                                   increment left by wordLen

4. If window length == totalLen:
       record index `left` as valid start

-----------------------------------------------------------
⏱ Time Complexity:
-----------------------------------------------------------
O(n * m)  
n = length of s  
m = number of words

-----------------------------------------------------------
💾 Space Complexity:
-----------------------------------------------------------
O(m) frequency dictionaries

-----------------------------------------------------------
"""
# ------------------------------------
# 30. Substring with Concatenation of All Words
# Sliding Window + Offset
# ------------------------------------

def findSubstring(s, words):
    result = []
    if not s or not words:
        return result

    # Build frequency map of words
    have = {}
    for w in words:
        have[w] = have.get(w, 0) + 1

    k = len(words[0])        # word length
    total_words = len(have)  # unique words
    n = len(s)

    # Loop over each offset
    for offset in range(k):
        left = right = offset
        count = 0
        seen = {}

        while right <= n - k:
            val = s[right:right+k]

            # Word not in dictionary → reset window
            if val not in have:
                seen.clear()
                count = 0
                left = right + k
                right += k
                continue

            # Add current word
            seen[val] = seen.get(val, 0) + 1
            if seen[val] == have[val]:
                count += 1

            # Shrink window if a word is over-counted
            while seen[val] > have[val]:
                leftval = s[left:left+k]
                if seen[leftval] == have[leftval]:
                    count -= 1
                seen[leftval] -= 1
                left += k

            # All unique words matched → record start index
            if count == total_words:
                result.append(left)

            right += k

    return result

# ------------------------------------
# Driver Test
# ------------------------------------

if __name__ == "__main__":
    print(findSubstring("barfoothefoobarman", ["foo","bar"]))        # [0, 9]
    print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))  # [6, 9, 12]
    print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))  # []
