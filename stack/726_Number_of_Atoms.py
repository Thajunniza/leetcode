"""

726. Number of Atoms

🧩 Problem:
You are given a chemical formula string (e.g., "H2O", "Mg(OH)2", "K4(ON(SO3)2)2") that may contain:
- Element symbols (an uppercase letter followed by zero or more lowercase letters), e.g., "H", "He", "Mg".
- Parentheses to group sub-formulas.
- Optional integer counts following elements or groups (default is 1 if missing).

Rules:
- Counts multiply for grouped expressions: "Mg(OH)2" ⇒ the group "(OH)" has count 2.
- Nested parentheses are possible, e.g., "K4(ON(SO3)2)2".
- The output must list elements in lexicographic order.
- Omit the count if it is 1.

🎯 Goal:
Parse the formula and return a canonical string of element counts, sorted lexicographically, omitting counts of 1.
Examples:
- "H2O"      → "H2O"
- "Mg(OH)2"  → "H2MgO2"
- "Be32"     → "Be32"
- "K4(ON(SO3)2)2" → "K4N2O14S4"

Algorithm — Stack-Based Parsing (Robust & Iterative):

Key observations:
- Element names are tokens: Capital + lowercase* (e.g., "Mg").
- Numbers (counts) are tokens: digits* (multi-digit allowed); default to 1 if absent.
- Parentheses introduce grouped counters that get multiplied when we see the closing ')'.

Approach:
1) Maintain a stack of counters (maps from element → count). Start with one empty counter on the stack.
2) Scan the string with an index `i`:
   - If we see `'('`: push a new empty counter (start a new group).
   - If we see `')'`: parse the number immediately after it (multiplier `mul`), pop the group counter, and add its counts multiplied by `mul` into the counter below.
   - Otherwise, we must be at an element name (uppercase), so:
     - Parse the full element name: Capital + lowercase*.
     - Parse the optional number that follows (default 1).
     - Add `num` to the top counter for that element.
3) At the end, the remaining top counter has the total counts. Format the result by sorting element names lexicographically and:
   - Append the element name.
   - Append the count only if > 1.

⏱ Time & Space Complexity:
Let n = len(formula).
- Time: O(n) for the single pass tokenization + O(m log m) for sorting `m` unique elements. Since m ≤ n, overall O(n log n) in worst case, typically close to linear.
- Space: O(n) for the stack and counters in worst case (deeply nested groups / many distinct elements).

Edge Cases:
- No counts ⇒ default to 1.
- Deeply nested parentheses.
- Multi-digit numbers (e.g., "O12").
- Single element (e.g., "C").
- Order only affects output sorting, not parsing.

"""


from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Parse a chemical formula and return the canonical string of atom counts,
        with elements sorted lexicographically and counts omitted if 1.
        """
        n = len(formula)
        i = 0
        stack = [Counter()]  # stack of counters; top is current group's counts

        def parse_name() -> str:
            """Parse element name: uppercase followed by zero or more lowercase letters."""
            nonlocal i
            start = i
            i += 1  # consume the uppercase letter
            while i < n and formula[i].islower():
                i += 1
            return formula[start:i]

        def parse_number() -> int:
            """Parse optional integer; default to 1 if absent."""
            nonlocal i
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            return int(formula[start:i]) if i > start else 1

        while i < n:
            ch = formula[i]
            if ch == '(':
                i += 1
                stack.append(Counter())
            elif ch == ')':
                i += 1
                mul = parse_number()
                group = stack.pop()
                for k, v in group.items():
                    stack[-1][k] += v * mul
            else:
                # Must be the start of an element name (uppercase letter)
                name = parse_name()
                num = parse_number()
                stack[-1][name] += num

        total = stack.pop()
        result = []
        # Format: lexicographic order; omit count if 1
        for k in sorted(total):
            val = total[k]
            if val > 1:
                result.append(k+str(val))
            else:
                result.append(k)
        return "".join(result)



# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("H2O", "H2O"),
        ("Mg(OH)2", "H2MgO2"),
        ("Be32", "Be32"),
        ("K4(ON(SO3)2)2", "K4N2O14S4"),
        ("(H)", "H"),
        ("((H)2O)3", "H6O3"),
        ("NaCl", "ClNa"),            # lexicographic order
        ("Fe2(SO4)3", "Fe2O12S3"),   # classic: ferric sulfate
        ("C", "C"),
        ("B2(He3C)4", "B2C4He12"),
    ]

    for formula, expected in tests:
        out = sol.countOfAtoms(formula)
        print(f"{formula:15s} -> {out:15s} | expected: {expected}")
        assert out == expected

    print("All tests passed!")
