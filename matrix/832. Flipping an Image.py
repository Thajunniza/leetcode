# ===========================================================
# 832. Flipping an Image
# ===========================================================

# 🧩 Problem:
# Given a binary matrix, flip each row horizontally and then invert it.
# Return the resulting matrix.

# -----------------------------------------------------------
# ⏱ Time Complexity:   O(m × n)
# 💾 Space Complexity: O(1)
# -----------------------------------------------------------

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            l, r = 0, len(row) - 1

            while l <= r:
                # Swap
                row[l], row[r] = row[r], row[l]

                # Invert
                row[l] ^= 1
                if l != r:
                    row[r] ^= 1

                l += 1
                r -= 1

        return image


# -----------------------------------------------------------
# Driver Code
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    image = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]
    print(sol.flipAndInvertImage(image))
    # Expected Output:
    # [
    #   [1, 0, 0],
    #   [0, 1, 0],
    #   [1, 1, 1]
    # ]
