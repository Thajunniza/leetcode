"""
2951: Find the Peaks

Given an integer array 'mountain', return the indices of all peak elements.
An element is a peak if it is strictly greater than its neighbors.
- The first and last elements are compared only with their single neighbor.

Example:
Input: mountain = [1, 3, 2, 4, 1]
Output: [1, 3]
Explanation: 
- mountain[1] = 3 > neighbors 1 and 2
- mountain[3] = 4 > neighbors 2 and 1

Algorithm:
1. Initialize an empty list `res`.
2. Iterate over all indices:
   - Compare current element with previous and next element.
   - If greater than both neighbors, append index to `res`.
3. Return `res`.

Time Complexity: O(n)
Space Complexity: O(1) (excluding output list)
"""

class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        n = len(mountain)
        res = []
        for i in range(n):
            prev = mountain[i-1] if i > 0 else float("-inf")
            nxt = mountain[i+1] if i + 1 < n else float("-inf")
            val = mountain[i]
            if val > prev and val > nxt:
                res.append(i)
        return res


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    assert sol.findPeaks([1, 3, 2, 4, 1]) == [1, 3]
    assert sol.findPeaks([0, 1, 0]) == [1]
    assert sol.findPeaks([1, 2, 3, 1]) == [2]
    assert sol.findPeaks([1]) == [0]
    assert sol.findPeaks([1, 2]) == [1]
    assert sol.findPeaks([2, 1]) == [0]

    print("All test cases passed!")
