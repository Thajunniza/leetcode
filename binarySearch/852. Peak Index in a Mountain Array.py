"""
852: Peak Index in a Mountain Array

Given a mountain array `arr`, return the index of the peak element.
A mountain array satisfies arr[0] < arr[1] < ... < arr[peak] > arr[peak+1] > ... > arr[n-1].

Algorithm (Binary Search):
1. Use binary search on the array:
   - Compare middle element with its next element.
   - If arr[mid] < arr[mid+1], peak is to the right → l = mid + 1
   - Else, peak is at mid or to the left → r = mid
2. Loop until l == r → peak index found.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                # Peak is to the right
                l = mid + 1
            else:
                # Peak is at mid or to the left
                r = mid

        return l  # l == r, peak index found


# ----------------- Test Cases -----------------
if __name__ == "__main__":
    sol = Solution()
    
    arr1 = [0, 2, 5, 3, 1]
    print(f"Peak index: {sol.peakIndexInMountainArray(arr1)}, value: {arr1[sol.peakIndexInMountainArray(arr1)]}")
    
    arr2 = [0, 10, 5, 2]
    print(f"Peak index: {sol.peakIndexInMountainArray(arr2)}, value: {arr2[sol.peakIndexInMountainArray(arr2)]}")
    
    arr3 = [-3, -1, 0, 2, 1, -2]
    print(f"Peak index: {sol.peakIndexInMountainArray(arr3)}, value: {arr3[sol.peakIndexInMountainArray(arr3)]}")
