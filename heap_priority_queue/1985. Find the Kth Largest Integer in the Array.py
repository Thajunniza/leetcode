"""
===========================================================
1985. Find the Kth Largest Integer in the Array
===========================================================

Problem:
Given an array of strings nums where each string represents
a non-negative integer, return the kth largest integer
as a string.

Note:
- The numbers can be very large (bigger than standard int).
- k is always valid (1 <= k <= len(nums)).

-----------------------------------------------------------
Example:
-----------------------------------------------------------
Input: nums = ["3","6","7","10"], k = 4
Output: "3"

Explanation:
Sorted descending: ["10","7","6","3"]
4th largest → "3"

-----------------------------------------------------------
Algorithm / Approach:
-----------------------------------------------------------
Two common approaches:

1️⃣ Heap Approach (Min-Heap of size k)
   - Maintain a min-heap of the k largest numbers.
   - Iterate over nums:
       - Push number into heap (convert to int in Python)
       - If heap size > k → pop smallest
   - Heap root at the end = kth largest.
   - Efficient when n is large and k is small.

2️⃣ Sorting Approach
   - Convert all nums to integers (Python handles big ints)
   - Sort descending
   - Return nums[k-1]
   - Often faster in Python due to C-implementation of sort.

-----------------------------------------------------------
Time Complexity:
-----------------------------------------------------------
Heap Approach:
- Push/pop n elements into heap of size k → O(n log k)
- Space: O(k)

Sorting Approach:
- Sort n elements → O(n log n)
- Space: O(n) (for int conversion list)

-----------------------------------------------------------
Space Complexity:
-----------------------------------------------------------
Heap: O(k)
Sorting: O(n)
"""

import heapq
import time

class Solution:

    # ------------------ Heap Approach ------------------
    def kthLargestNumber_heap(self, nums, k):
        """
        Min-Heap approach
        """
        minH = []

        for val in nums:
            heapq.heappush(minH, int(val))  # convert to int
            if len(minH) > k:
                heapq.heappop(minH)

        return str(minH[0])

    # ------------------ Sorting Approach ------------------
    def kthLargestNumber_sort(self, nums, k):
        """
        Sorting approach
        """
        nums_int = [int(x) for x in nums]
        nums_int.sort(reverse=True)
        return str(nums_int[k-1])

    # ------------------ String-Only Sorting (Optional) ------------------
    def kthLargestNumber_string(self, nums, k):
        """
        Sorting strings without int conversion
        Works even if numbers are extremely large
        """
        nums.sort(key=lambda x: (len(x), x))  # sort by length, then lex
        return nums[-k]  # kth largest

# ===================== Test Cases =====================
def run_tests():
    sol = Solution()
    test_cases = [
        (["3","6","7","10"], 4, "3"),
        (["2","21","12","1"], 3, "2"),
        (["1","2","3","4","5"], 1, "5"),
        (["100","200","50","20","300"], 2, "200"),
        (["12345678901234567890","98765432109876543210","1"], 1, "98765432109876543210"),
    ]

    print("\n------ Running Test Cases ------\n")
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        # Heap
        start = time.time()
        heap_res = sol.kthLargestNumber_heap(nums[:], k)
        heap_time = time.time() - start

        # Sort
        start = time.time()
        sort_res = sol.kthLargestNumber_sort(nums[:], k)
        sort_time = time.time() - start

        # String-only sorting
        start = time.time()
        string_res = sol.kthLargestNumber_string(nums[:], k)
        string_time = time.time() - start

        print(f"Test Case {i}: nums={nums}, k={k}")
        print(f"  Expected: {expected}")
        print(f"  Heap Result: {heap_res} | Time: {heap_time:.6f}s | {'PASS' if heap_res == expected else 'FAIL'}")
        print(f"  Sort Result: {sort_res} | Time: {sort_time:.6f}s | {'PASS' if sort_res == expected else 'FAIL'}")
        print(f"  String-Only Sort Result: {string_res} | Time: {string_time:.6f}s | {'PASS' if string_res == expected else 'FAIL'}")
        print("-"*80)

if __name__ == "__main__":
    run_tests()