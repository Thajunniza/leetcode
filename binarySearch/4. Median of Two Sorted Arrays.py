"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n, return the median 
of the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5

---

Algorithms:

1. Brute-force Merge:
   - Merge both arrays using two pointers.
   - Compute median from merged array.
   - Time Complexity: O(m + n)
   - Space Complexity: O(m + n)

2. Optimized Binary Search:
   - Binary search on the smaller array to find the correct partition.
   - Check: max(left halves) <= min(right halves)
   - Odd length: median = min(first element of right partition)
   - Even length: median = average of max(left halves) and min(right halves)
   - Time Complexity: O(log(min(m,n)))
   - Space Complexity: O(1)
"""

class Solution(object):
    # ----------------- Brute-force solution -----------------
    def findMedianSortedArraysBruteForce(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        merged = [0] * n
        i = j = k = 0
        
        # Merge arrays
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                merged[k] = nums1[i]
                i += 1
            else:
                merged[k] = nums2[j]
                j += 1
            k += 1

        while i < n1:
            merged[k] = nums1[i]
            i += 1
            k += 1
        while j < n2:
            merged[k] = nums2[j]
            j += 1
            k += 1

        # Find median
        if n % 2 == 0:
            mid = n // 2
            return (merged[mid-1] + merged[mid]) / 2.0
        else:
            mid = n // 2
            return float(merged[mid])

    # ----------------- Optimized solution -----------------
    def findMedianSortedArraysOptimal(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        # Ensure a is smaller
        if n1 <= n2:
            a, b = nums1, nums2
        else:
            a, b = nums2, nums1
            n1, n2 = n2, n1

        total = n1 + n2
        half = total // 2
        l, r = 0, n1 - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            aleft = a[i] if i >= 0 else float("-inf")
            aright = a[i+1] if i+1 < n1 else float("inf")
            bleft = b[j] if j >= 0 else float("-inf")
            bright = b[j+1] if j+1 < n2 else float("inf")

            if aleft <= bright and bleft <= aright:
                if total % 2:  # odd length
                    return float(min(aright, bright))
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2.0
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1

        raise ValueError("Input arrays are not valid")


# ----------------- Test Cases -----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1,3], [2]),
        ([1,2], [3,4]),
        ([], [1]),
        ([2], []),
        ([0,0], [0,0]),
    ]

    print("----- Brute-force Results -----")
    for nums1, nums2 in test_cases:
        print(f"{nums1} + {nums2} => {sol.findMedianSortedArraysBruteForce(nums1, nums2)}")

    print("\n----- Optimized Results -----")
    for nums1, nums2 in test_cases:
        print(f"{nums1} + {nums2} => {sol.findMedianSortedArraysOptimal(nums1, nums2)}")
