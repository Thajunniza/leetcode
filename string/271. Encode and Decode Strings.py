"""
===========================================================
271. Encode and Decode Strings
===========================================================

🧩 Problem:
Design an algorithm to encode a list of strings into a
single string and decode it back to the original list.

The encoding must be unambiguous and work for any
possible characters (including digits, '#', spaces, etc.).

-----------------------------------------------------------
Approach — Length Prefix Encoding
-----------------------------------------------------------

Key idea:
For each string, store:

    <length>#<string>

Example:
["lint", "code"]  →  "4#lint4#code"

During decoding:
1. Read digits until '#'
2. Convert to integer (length)
3. Read exactly 'length' characters
4. Repeat

This avoids ambiguity even if the string contains '#'
or digits.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(n)
-----------------------------------------------------------
"""

class Codec(object):

    def encode(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + "#" + s)

        return "".join(encoded)

    def decode(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(s)

        while i < n:
            # Step 1: Read length
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Step 2: Extract string
            i = j + 1
            res.append(s[i:i + length])

            # Step 3: Move pointer
            i += length

        return res


# ==========================
# ✅ Test Cases
# ==========================
if __name__ == "__main__":
    codec = Codec()

    test_cases = [
        (["lint", "code", "love", "you"], ["lint", "code", "love", "you"]),
        ([""], [""]),
        (["#"], ["#"]),
        (["123", "abc"], ["123", "abc"]),
        ([], []),
    ]

    for strs, expected in test_cases:
        encoded = codec.encode(strs)
        decoded = codec.decode(encoded)

        print("Input:     ", strs)
        print("Encoded:   ", encoded)
        print("Decoded:   ", decoded)
        print("Expected:  ", expected)
        print("Pass:      ", decoded == expected)
        print("-" * 40)
