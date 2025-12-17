"""
# ------------------------------------------------------------
# 763. Partition Labels
#
# Problem:
#   Given a string s, partition it into as many parts as possible so that
#   each letter appears in at most one part. Return a list of partition sizes.
#
# Algorithm (Last Occurrence + Greedy Expand Window):
#   1) Build last[ch] = last index where character ch appears in s.
#   2) Scan s left to right, maintaining a window [start..end]:
#        - end = max(end, last[s[i]])  (expand window to include all future occurrences)
#        - When i == end, we can close this partition:
#             size = end - start + 1
#             append size, set start = i + 1
#
# Time:  O(n)
# Space: O(1) typical (bounded alphabet) / O(k) for distinct chars
#
# Logic Hint:
#   Keep extending the current segment’s end to the farthest last occurrence
#   of any character seen so far. When the scan reaches that end, cut.
# ------------------------------------------------------------
"""
class Solution(object):
    def partitionLabels(self, s):
        # 1) last occurrence of each character
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        # 2) greedy partitioning
        res = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res


# ------------------------------------------------------------
# Driver Tests
# ------------------------------------------------------------
def run_tests():
    sol = Solution()
    cases = [
        ("ababcbacadefegdehijhklij", [9, 7, 8]),
        ("eccbbbbdec", [10]),
        ("abc", [1, 1, 1]),
        ("aaaaa", [5]),
        ("", []),
    ]

    for s, expected in cases:
        out = sol.partitionLabels(s)
        print(f"Input:    {s!r}")
        print(f"Output:   {out}")
        print(f"Expected: {expected}")
        print("----")

if __name__ == "__main__":
    run_tests()

