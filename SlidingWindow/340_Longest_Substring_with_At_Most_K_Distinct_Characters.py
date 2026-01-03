"""
===========================================================
340 - Longest Substring with At Most K Distinct Characters
===========================================================

🧩 Problem:
Given a string s and an integer k, return the length of the longest 
substring of s that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Example 3:
Input: s = "eceba", k = 3
Output: 4
Explanation: The substring is "eceb" with length 4.

-----------------------------------------------------------
Approach — Sliding Window with HashMap:
-----------------------------------------------------------
Use a sliding window with two pointers to maintain a valid substring:

1. Expand window (move right pointer):
   - Add character to frequency map using enumerate
   - Track distinct characters in hashmap

2. Shrink window when invalid (> k distinct):
   - Remove leftmost character by decrementing frequency
   - If frequency becomes 0, remove from map
   - Move left pointer forward

3. Track maximum window size throughout

Key insight: Use hashmap size to count distinct characters.
When len(seen) > k, we need to shrink the window.

Visual Example:
s = "eceba", k = 2

Step 1: [e]ceba → {e:1} → 1 distinct, len=1, result=1
Step 2: [ec]eba → {e:1,c:1} → 2 distinct, len=2, result=2
Step 3: [ece]ba → {e:2,c:1} → 2 distinct, len=3, result=3 ✓
Step 4: [eceb]a → {e:2,c:1,b:1} → 3 distinct > k!
        Shrink: e[ceb]a → {e:1,c:1,b:1} → still 3 > k
        Shrink: ec[eb]a → {e:1,b:1} → 2 distinct, len=2
Step 5: ec[eba] → {e:2,b:1,a:1} → 3 distinct > k!
        Shrink: ece[ba] → {e:1,b:1,a:1} → still 3 > k
        Shrink: eceb[a] → {a:1} → 1 distinct, len=1

Max length = 3

-----------------------------------------------------------
⏱ Time Complexity:   O(n)    # each character visited at most twice
💾 Space Complexity:  O(k)    # at most k+1 distinct chars in map
-----------------------------------------------------------
"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        seen = {}
        left = 0
        result = 0
        
        for right, val in enumerate(s):
            # Expand window: add current character
            seen[val] = seen.get(val, 0) + 1
            
            # Shrink window while we have more than k distinct characters
            while len(seen) > k:
                leftval = s[left]
                seen[leftval] -= 1
                if seen[leftval] == 0:
                    del seen[leftval]
                left += 1
            
            # Update result with current window size
            result = max(result, (right - left + 1))
        
        return result


# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 2))
    # Expected Output: 3 ("ece")
    
    # Example 2
    print(sol.lengthOfLongestSubstringKDistinct("aa", 1))
    # Expected Output: 2 ("aa")
    
    # Example 3
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 3))
    # Expected Output: 4 ("eceb")
    
    # Edge case: k = 0
    print(sol.lengthOfLongestSubstringKDistinct("eceba", 0))
    # Expected Output: 0
    
    # All same characters
    print(sol.lengthOfLongestSubstringKDistinct("aaaaaaa", 1))
    # Expected Output: 7
    
    # Single character
    print(sol.lengthOfLongestSubstringKDistinct("a", 2))
    # Expected Output: 1