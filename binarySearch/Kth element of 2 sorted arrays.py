"""
Problem:
K-th Element of Two Sorted Arrays (Index-Style Binary Search)

Given two sorted arrays a and b, find the k-th smallest element
in the combined sorted array.
k is 1-indexed.

Example:
Input:
a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

Output:
6
"""

class Solution:
    def kthElement(self, a, b, k):
        """
        Time Complexity: O(log(min(n1, n2)))
        Space Complexity: O(1)
        """

        n1 = len(a)
        n2 = len(b)

        # Always binary search on smaller array
        if n1 > n2:
            a, b = b, a
            n1, n2 = n2, n1

        # Index-style binary search bounds
        # i and j are indices of last elements on left partition
        l = max(-1, k - n2 - 1)
        r = min(k - 1, n1 - 1)

        while l <= r:
            i = (l + r) // 2
            j = k - i - 2

            # Left partition elements
            aleft = a[i] if i >= 0 else float("-inf")
            bleft = b[j] if j >= 0 else float("-inf")

            # Right partition elements
            aright = a[i + 1] if i + 1 < n1 else float("inf")
            bright = b[j + 1] if j + 1 < n2 else float("inf")

            # Valid partition condition
            if aleft <= bright and bleft <= aright:
                # k-th element is the maximum on the left side
                return max(aleft, bleft)

            # Move left in array a
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1

        return -1


# ---------------- Test Cases ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.kthElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # 6
    print(sol.kthElement([1, 3], [2], 2))                  # 2
    print(sol.kthElement([1, 2], [3, 4], 3))               # 3
    print(sol.kthElement([], [1, 2, 3], 1))                # 1
    print(sol.kthElement([5], [], 1))                      # 5
