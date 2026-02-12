# ===========================================================
# 1124. Longest Well-Performing Interval
# ===========================================================

# Problem:
# --------
# You are given an integer array hours where hours[i] is the number of hours the i-th employee worked on the i-th day.

# A day is considered tiring if hours[i] > 8.

# Return the length of the longest well-performing interval (a contiguous subarray) such that the number of tiring days is strictly greater than the number of non-tiring days.

# -----------------------------------------------------------
# Approach 1: Prefix Sum + Earliest Index (Hash Map)
# -----------------------------------------------------------

# Key Idea:
# ---------
# Map each day to:
#     +1 if hours[i] > 8   (tiring)
#     -1 otherwise         (non-tiring)

# Let s be the running prefix sum.

# Observation:
#     For a subarray (l+1 .. r) to be well-performing:
#         prefix[r] - prefix[l] > 0
#     ⟺  prefix[r] > prefix[l]

# We want the longest such interval for each r.
# Two cases:
#   1) If s > 0:
#        The whole prefix [0..r] is already valid → answer can be r+1
#   2) Otherwise:
#        Try to find the earliest index l where prefix[l] = s - 1
#        Then (l+1 .. r) has sum > 0 and is as long as possible for this r.

# We maintain a hash map:
#     first[value] = earliest index where this prefix sum appeared

# Never overwrite first[value] once set (we need the earliest to maximize length).

# Time Complexity: O(n)
# Space Complexity: O(n)

class SolutionHashMap(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        ans = 0
        first = {}   # prefix value -> earliest index
        s = 0        # running prefix sum (+1 for >8, -1 otherwise)

        for i, h in enumerate(hours):
            s += 1 if h > 8 else -1

            # Case 1: whole prefix [0..i] is well-performing
            if s > 0:
                ans = i + 1
            else:
                # Case 2: look for earliest prefix == s - 1
                if (s - 1) in first:
                    ans = max(ans, i - first[s - 1])

            # Record earliest occurrence of this prefix sum
            if s not in first:
                first[s] = i

        return ans

# -----------------------------
# Test Case
# -----------------------------
if __name__ == "__main__":
    tests = [
        ([9, 9, 6, 0, 6, 6, 9], 3),
        ([6, 6, 6], 0),
        ([9, 9, 9], 3),
        ([9, 6, 9], 3),
        ([8, 9, 9], 2),
        ([6, 9], 1),          # single tiring day
        ([6, 9, 6, 9], 3),
    ]

    hm = SolutionHashMap()

    for arr, exp in tests:
        print("hours:", arr)
        print("  HashMap       ->", hm.longestWPI(arr), " expected:", exp)
        print("-" * 40)