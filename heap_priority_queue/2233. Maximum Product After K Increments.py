"""
===========================================================
2233. Maximum Product After K Increments
===========================================================

Problem:
Given an integer array nums and an integer k, you can increment
any element by 1 exactly k times. Return the maximum product
of all elements after k increments, modulo 10^9 + 7.

-----------------------------------------------------------
Example:
-----------------------------------------------------------
Input: nums = [1,2,3], k = 3
Output: 27
Explanation:
Increment smallest element each time:
[1,2,3] → [2,2,3] → [3,2,3] → [3,3,3]
Product = 3*3*3 = 27
"""

import heapq

class Solution:
    """
    Algorithm (Greedy + Min-Heap):
    1. Convert nums into a min-heap (O(n)) to efficiently track the smallest number.
    2. Repeat k times:
       a. Pop the smallest element from the heap.
       b. Increment it by 1.
       c. Push it back into the heap (O(log n) per operation).
    3. Multiply all elements in the heap and return modulo 10^9+7.
    
    Time Complexity: O(n + k log n)
        - Heapify: O(n)
        - k increments: O(k log n)
        - Product calculation: O(n)
        - Total: O(n + k log n)
    
    Space Complexity: O(1) extra (heap is in-place)
    """

    def maximumProduct(self, nums, k):
        mod = 10**9 + 7
        
        # Step 1: heapify
        heapq.heapify(nums)  # O(n)
        
        # Step 2: increment smallest element k times
        for _ in range(k):
            val = heapq.heappop(nums)  # O(log n)
            heapq.heappush(nums, val + 1)  # O(log n)
        
        # Step 3: calculate product with modulo
        product = 1
        for val in nums:  # O(n)
            product = (product * val) % mod
        
        return product

# ===================== Test Cases =====================
def run_tests():
    sol = Solution()
    test_cases = [
        ([1,2,3], 3, 27),
        ([1,4,3,2], 5, 192),
        ([1,1,1], 3, 8),
        ([2,3,5], 0, 30),
        ([10**5, 10**5, 10**5], 3, (100001*100000*100000) % (10**9+7))
    ]
    
    print("\n------ Running Test Cases ------\n")
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = sol.maximumProduct(nums[:], k)
        print(f"Test Case {i}: nums={nums}, k={k}")
        print(f"  Expected: {expected}")
        print(f"  Result:   {result} | {'PASS' if result == expected else 'FAIL'}")
        print("-"*60)

if __name__ == "__main__":
    run_tests()