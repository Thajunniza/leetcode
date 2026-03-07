"""
===========================================================
832. Flipping an Image
===========================================================

🧩 Problem:
Given an n x n binary matrix `image`, flip the image horizontally,
then invert it.

1. Flip horizontally → reverse each row.
2. Invert the image → replace:
      0 → 1
      1 → 0

Return the resulting image.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------
Input:
image = [[1,1,0],
         [1,0,1],
         [0,0,0]]

Output:
[[1,0,0],
 [0,1,0],
 [1,1,1]]

Explanation:
Step 1 — Flip Horizontally
[1,1,0] → [0,1,1]

Step 2 — Invert
[0,1,1] → [1,0,0]

-----------------------------------------------------------
Algorithm — Two Pointer + XOR
-----------------------------------------------------------
Idea:

1. Use two pointers `l` and `r` to reverse each row.
2. While swapping the elements, invert them using XOR.
3. XOR with 1 flips a bit:
        0 ^ 1 = 1
        1 ^ 1 = 0
4. If the row length is odd, the middle element remains unswapped,
   so we invert it separately.

Key Insight:
- Combine **flip + invert in one step** during the swap.
- This avoids an extra pass over the array.
- XOR is used because it flips binary values efficiently.

-----------------------------------------------------------
⏱ Time Complexity:   O(n * m)
💾 Space Complexity:  O(1)   (in-place modification)
-----------------------------------------------------------
"""

# ------------------------------------
# Solution: Two Pointer + XOR
# ------------------------------------
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image[0]) - 1

        for i, row in enumerate(image):

            l = 0
            r = n

            while l < r:
                image[i][l], image[i][r] = image[i][r] ^ 1, image[i][l] ^ 1
                l += 1
                r -= 1

            if l == r:
                image[i][l] ^= 1

        return image


# ------------------------------------
# Driver Test
# ------------------------------------
if __name__ == "__main__":

    sol = Solution()

    image1 = [[1,1,0],
              [1,0,1],
              [0,0,0]]

    image2 = [[1,1,0,0],
              [0,1,1,0],
              [1,0,0,1],
              [0,0,1,1]]

    print(sol.flipAndInvertImage(image1))
    # Expected Output:
    # [[1,0,0],[0,1,0],[1,1,1]]

    print(sol.flipAndInvertImage(image2))