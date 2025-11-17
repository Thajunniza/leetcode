"""
===========================================================
75. Sort Colors (Dutch National Flag Problem)
===========================================================

🧩 Problem:
Given an array 'colors' containing only values 0, 1, and 2,
sort the array in-place such that:
0s come first, then 1s, then 2s.

🎯 Goal:
Sort the array using the Dutch National Flag Algorithm
with O(n) time and O(1) extra space.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Example 1:
Input:  colors = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input:  colors = [2,0,1]
Output: [0,1,2]

Example 3:
Input:  colors = [0]
Output: [0]

Example 4:
Input:  colors = [1,2,0]
Output: [0,1,2]

-----------------------------------------------------------
Algorithm — Three Pointers (low, mid, high):
-----------------------------------------------------------
1. Use three pointers:
   - low  → next index to place a 0
   - mid  → current index being processed
   - high → next index to place a 2

2. Traverse while mid <= high:

   Case 0:
     - swap(colors[low], colors[mid])
     - low++, mid++
     - expands 0-region

   Case 1:
     - mid++
     - 1 belongs to middle region

   Case 2:
     - swap(colors[mid], colors[high])
     - high--
     - DO NOT increment mid (new value must be rechecked)

3. Continue until mid crosses high.

4. Return the sorted array.

-----------------------------------------------------------
⏱ Time Complexity:   O(n)
💾 Space Complexity:  O(1)
-----------------------------------------------------------
"""


# ------------------------------------
# Sort Colors (Dutch National Flag)
# colors = list of 0s, 1s, 2s
# return sorted list in-place
# ------------------------------------
def sort_colors(colors):
    low, mid, high = 0, 0, len(colors) - 1

    while mid <= high:
        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1

        elif colors[mid] == 1:
            mid += 1

        else:  # colors[mid] == 2
            colors[mid], colors[high] = colors[high], colors[mid]
            high -= 1

    return colors


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":
    arr = [2, 0, 1, 2, 0, 1]
    print("Input: ", arr)
    print("Sorted:", sort_colors(arr))
