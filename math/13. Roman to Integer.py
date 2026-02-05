"""
13. Roman to Integer

🧩 Problem:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer.

🎯 Goal:
Implement a function that translates the string representation of a Roman numeral 
into its corresponding integer value, handling the subtraction cases (like IV or IX).

***

## Algorithm — Right-to-left scan with comparison:

1.  **Values**: Map each Roman symbol to its integer value.
2.  **Initialize**: Start the `total` with the value of the very last character.
3.  **Iterate Backwards**: Loop from the second-to-last character back to the start.
4.  **Evaluate**:
    *   If `current_val < next_val`: Subtraction rule (e.g., IV).
    *   Else: Standard addition.

***

⏱ Time Complexity: O(n)
💾 Space Complexity: O(1)

***
"""

# ------------------------------------
# Roman to Integer — Meaningful Names
# ------------------------------------

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        n = len(s)
        # Start with the rightmost value
        total = roman[s[n - 1]]
        
        # Traverse backwards from the second-to-last character
        for i in range(n - 2, -1, -1):
            current_val = roman[s[i]]
            next_val = roman[s[i + 1]]
            
            if current_val < next_val:
                total -= current_val
            else:
                total += current_val
                
        return total

# ------------------------------------
# Driver Tests
# ------------------------------------

def run_tests():
    cases = [
        "III",        # Expected: 3
        "LVIII",      # Expected: 58
        "MCMXCIV",    # Expected: 1994
    ]
    
    sol = Solution()
    for roman_str in cases:
        result = sol.romanToInt(roman_str)
        print(f"Input:  {roman_str}\nOutput: {result}\n")

if __name__ == "__main__":
   run_tests()
