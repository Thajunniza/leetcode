# ------------------------------------------------------------
# Find Number of Rotations in Rotated Sorted Array
# ------------------------------------------------------------
# Problem:
# Given a sorted array that has been rotated unknown times,
# find the number of rotations. The number of rotations
# equals the index of the minimum element.
#
# Example:
# Input:  arr = [15, 18, 2, 3, 6, 12]
# Output: 2
#
# Input:  arr = [7, 9, 11, 12, 5]
# Output: 4
#
# Input:  arr = [1, 2, 3, 4, 5]
# Output: 0
#
# Algorithm (Binary Search):
# 1. Initialize left = 0, right = len(arr) - 1
# 2. Maintain a variable min_val to track the minimum
#    and rotation_index to track its index
# 3. While left <= right:
#    - Compute mid
#    - If left half is sorted (arr[left] <= arr[mid]):
#         - Update min_val and rotation_index if arr[left] is smaller
#         - Search right half (left = mid + 1)
#    - Else (left half unsorted):
#         - Update min_val and rotation_index if arr[mid] is smaller
#         - Search left half (right = mid - 1)
# 4. Return rotation_index
# ------------------------------------------------------------

class Solution:
    def findKRotation(self, arr):
        """
        :param arr: List[int] - rotated sorted array (unique elements)
        :return: int - number of rotations = index of minimum element
        """
        l, r = 0, len(arr) - 1
        min_val = float("inf")
        rotation_index = 0
        
        while l <= r:
            mid = (l + r) // 2
            
            # Left half is sorted
            if arr[l] <= arr[mid]:
                if arr[l] < min_val:
                    min_val = arr[l]
                    rotation_index = l
                l = mid + 1
            else:
                # Minimum is in left half
                if arr[mid] < min_val:
                    min_val = arr[mid]
                    rotation_index = mid
                r = mid - 1
                
        return rotation_index

# ------------------------------------------------------------
# Test Run
# ------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        [15, 18, 2, 3, 6, 12],   # rotated 2 times
        [7, 9, 11, 12, 5],       # rotated 4 times
        [1, 2, 3, 4, 5],         # rotated 0 times
        [4, 5, 1, 2, 3],         # rotated 2 times
    ]
    
    for arr in test_cases:
        print(f"Array: {arr} -> Rotations: {sol.findKRotation(arr)}")