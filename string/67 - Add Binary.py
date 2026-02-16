# ===========================================================
# 67 - Add Binary
# ===========================================================

# 🧩 Problem:
# Given two binary strings a and b,
# return their sum as a binary string.

# 🎯 Goal:
# Perform binary addition and return the result as a string.

# -----------------------------------------------------------
# Examples:
# -----------------------------------------------------------

# Input:  a = "11", b = "1"
# Output: "100"

# Input:  a = "1010", b = "1011"
# Output: "10101"

# -----------------------------------------------------------
# Algorithm — Manual Binary Addition (Optimal):
# -----------------------------------------------------------
# 1. Initialize two pointers i and j at the end of strings.
# 2. Maintain a variable `carry = 0`.
# 3. While i >= 0 OR j >= 0 OR carry exists:
#    a. total = carry
#    b. Add a[i] if i >= 0
#    c. Add b[j] if j >= 0
#    d. Append (total % 2) to result
#    e. carry = total // 2
# 4. Reverse result and return as string.

# ⏱ Time Complexity:   O(max(n, m))
# 💾 Space Complexity:  O(max(n, m))

# -----------------------------------------------------------
# Algorithm — Built-in Conversion (Simple):
# -----------------------------------------------------------
# 1. Convert binary strings to integers using int(x, 2).
# 2. Add them.
# 3. Convert back using bin() and remove "0b".

# ⏱ Time Complexity:   O(max(n, m))
# 💾 Space Complexity:  O(max(n, m))
# -----------------------------------------------------------


# ------------------------------------
# Solution 1: Manual Binary Addition
# ------------------------------------
class SolutionManual(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            res.append(str(total % 2))
            carry = total // 2

        return "".join(res[::-1])


# ------------------------------------
# Solution 2: Built-in Conversion
# ------------------------------------
class SolutionBuiltin(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


# ------------------------------------
# Driver Tests
# ------------------------------------
if __name__ == "__main__":
    a1, b1 = "11", "1"
    a2, b2 = "1010", "1011"

    print("Manual Solution:")
    sol1 = SolutionManual()
    print(sol1.addBinary(a1, b1))  # Output: "100"
    print(sol1.addBinary(a2, b2))  # Output: "10101"

    print("\nBuilt-in Solution:")
    sol2 = SolutionBuiltin()
    print(sol2.addBinary(a1, b1))  # Output: "100"
    print(sol2.addBinary(a2, b2))  # Output: "10101"
