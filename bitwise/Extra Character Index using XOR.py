# ===========================================================
# Extra Character Index using XOR
# ===========================================================

# 🧩 Problem:
# Given two strings str1 and str2 where str2 has exactly one extra
# character compared to str1, return the index of the extra character
# in str2.

# -----------------------------------------------------------
# Examples:
# -----------------------------------------------------------
# str1 = "abcd", str2 = "abecd" → Output: 2
# str1 = "xyz", str2 = "xayz" → Output: 1
# str1 = "", str2 = "a" → Output: 0

# -----------------------------------------------------------
# Algorithm — XOR Trick:
# -----------------------------------------------------------
# 1. XOR all characters of str1 and str2
# 2. All common characters cancel out
# 3. Remaining XOR gives the ASCII of extra character
# 4. Use str2.index(extra_char) to get its index

def extra_character_index(str1, str2):
    # Ensure str2 is the longer string
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    xor = 0
    for c in str1:
        xor ^= ord(c)
    for c in str2:
        xor ^= ord(c)

    extra_char = chr(xor)
    return str2.index(extra_char)


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    print(extra_character_index("abcd", "abecd"))  # Expected Output: 2
    print(extra_character_index("xyz", "xayz"))    # Expected Output: 1
    print(extra_character_index("", "a"))          # Expected Output: 0
    print(extra_character_index("aaaa", "aaaaa"))  # Expected Output: 4