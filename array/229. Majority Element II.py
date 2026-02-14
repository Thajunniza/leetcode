"""
===========================================================
229. Majority Element II
===========================================================

🧩 Problem:
Given an integer array nums, return all elements that appear more than n/3 times.

-----------------------------------------------------------
Solution 1: Sorting + Frequency Count
-----------------------------------------------------------
- Sort the array
- Count consecutive duplicates
- Append elements appearing more than n//3

Time Complexity: O(n log n)
Space Complexity: O(1) (excluding sorting)
-----------------------------------------------------------
"""

class SolutionSorting(object):
    def majorityElement(self, nums):
        n = len(nums)
        need = n // 3
        nums.sort()

        res = []
        l = 0
        i = 0
        while i < n:
            while i < n and nums[l] == nums[i]:
                i += 1
            if (i - l) > need:
                res.append(nums[l])
            l = i

        return res


"""
-----------------------------------------------------------
Solution 2: Boyer-Moore Voting Algorithm (O(n) Optimal)
-----------------------------------------------------------
- Track at most 2 candidates
- Cancel out counts for different elements
- Verify actual counts in second pass

Time Complexity: O(n)
Space Complexity: O(1)
-----------------------------------------------------------
"""

class SolutionBoyerMoore(object):
    def majorityElement(self, nums):
        c1 = c2 = 0
        e1 = e2 = None

        # First pass: find potential candidates
        for val in nums:
            if val == e1:
                c1 += 1
            elif val == e2:
                c2 += 1
            elif c1 == 0:
                e1 = val
                c1 = 1
            elif c2 == 0:
                e2 = val
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        # Second pass: verify counts
        res = []
        need = len(nums) // 3
        if e1 is not None and nums.count(e1) > need:
            res.append(e1)
        if e2 is not None and e2 != e1 and nums.count(e2) > need:
            res.append(e2)

        return res


# --------------------------
# Driver Tests
# --------------------------
if __name__ == "__main__":
    nums_list = [
        [3,2,3],
        [1,1,1,3,3,2,2,2],
        [1,2,3,4]
    ]

    print("=== Sorting Solution ===")
    sol_sort = SolutionSorting()
    for nums in nums_list:
        print(f"{nums} → {sol_sort.majorityElement(nums)}")

    print("\n=== Boyer-Moore Solution ===")
    sol_bm = SolutionBoyerMoore()
    for nums in nums_list:
        print(f"{nums} → {sol_bm.majorityElement(nums)}")
