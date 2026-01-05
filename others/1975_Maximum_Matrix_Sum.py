"""
===========================================================
1975. Maximum Matrix Sum
===========================================================

🧩 Problem:
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.

Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum 
sum of the matrix's elements using the operation mentioned above.

-----------------------------------------------------------
Example :
-----------------------------------------------------------
Example 1:
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
The final matrix is [[1,1],[1,1]] with sum = 4.

Example 2:
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following steps to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
The final matrix is [[1,2,3],[-1,2,3],[1,2,3]] with sum = 16.

Example 3:
Input: matrix = [[-1,0,-1],[-2,1,3]]
Output: 6

-----------------------------------------------------------
Brute Force Approach: Try All Possible Operations
-----------------------------------------------------------
1. Try all possible adjacent pairs
2. For each pair, multiply by -1 and recursively find max sum
3. Backtrack and try other combinations
4. Return maximum sum found

Problem: Exponential time complexity - not feasible
-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(2^(n²)) - exponential
Space: O(n²) - recursion depth

-----------------------------------------------------------
🧠 Key Observation and Optimal Approach
-----------------------------------------------------------
Key Insights:

1. When we flip two adjacent elements, we change their signs.
   Example: [a, b] becomes [-a, -b]

2. By doing multiple operations, we can "move" negative signs around:
   - Flip [a, -b] → [-a, b] (negative moved from right to left)
   - We can move negatives across the matrix!

3. Each operation flips TWO elements:
   - If both are negative: we get 2 positives (good!)
   - If both are positive: we get 2 negatives (bad!)
   - If one positive, one negative: we move the negative

4. CRITICAL INSIGHT:
   - If we have an EVEN number of negatives: we can eliminate ALL of them
     (pair them up and flip each pair)
   - If we have an ODD number of negatives: we must keep ONE negative
     (we can't eliminate the last one)

5. If we must keep one negative, which one?
   - Keep the negative on the SMALLEST absolute value to maximize sum!

Algorithm:
1. Count total number of negative values
2. Calculate sum of absolute values of all elements
3. Find the minimum absolute value in the matrix
4. If negative count is EVEN:
   - Return sum of absolute values (we can make all positive)
5. If negative count is ODD:
   - Return sum of absolute values - 2 * min_abs_value
   - (We subtract twice because we counted it as positive, now make it negative)

Special Case:
- If matrix contains 0, we can always achieve sum of absolute values
  (we can "trap" the negative at 0, effectively eliminating it)

Visual Example:
matrix = [[1,-1],[-1,1]]
Negative count = 2 (even)
Sum of absolute values = |1| + |-1| + |-1| + |1| = 4
Since even negatives, we can make all positive → result = 4

matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Negative count = 3 (odd)
Sum of absolute values = 1+2+3+1+2+3+1+2+3 = 18
Min absolute value = 1
Result = 18 - 2*1 = 16 (keep one negative on smallest value)

-----------------------------------------------------------
⏱️ Time & Space Complexity
-----------------------------------------------------------
Time:  O(n²) where n is the size of matrix
Space: O(1)

"""

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        
        # Count negative numbers
        negative_count = 0
        
        # Sum of absolute values
        total_sum = 0
        
        # Track minimum absolute value
        min_abs_value = float('inf')
        
        # Traverse the matrix
        for i in range(n):
            for j in range(n):
                value = matrix[i][j]
                
                # Count negatives
                if value < 0:
                    negative_count += 1
                
                # Add absolute value to sum
                abs_value = abs(value)
                total_sum += abs_value
                
                # Track minimum absolute value
                min_abs_value = min(min_abs_value, abs_value)
        
        # If even number of negatives, we can eliminate all
        if negative_count % 2 == 0:
            return total_sum
        
        # If odd number of negatives, we must keep one negative
        # Keep it on the smallest absolute value
        return total_sum - 2 * min_abs_value

# -----------------------------------------------------------
# Driver Examples
# -----------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: Even negatives
    print("=== Example 1 ===")
    matrix = [[1, -1], [-1, 1]]
    result = sol.maxMatrixSum(matrix)
    print(f"Input: {matrix}")
    print(f"Output: {result}")
    print(f"Expected: 4")
    print(f"Explanation: 2 negatives (even) -> can make all positive")
    
    # Example 2: Odd negatives
    print("\n=== Example 2 ===")
    matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
    result = sol.maxMatrixSum(matrix)
    print(f"Input: {matrix}")
    print(f"Output: {result}")
    print(f"Expected: 16")
    print(f"Explanation: 3 negatives (odd) -> keep one negative on min value (1)")
    
    # Example 3: Contains zero
    print("\n=== Example 3 ===")
    matrix = [[-1, 0, -1], [-2, 1, 3]]
    result = sol.maxMatrixSum(matrix)
    print(f"Input: {matrix}")
    print(f"Output: {result}")
    print(f"Expected: 6")
    print(f"Explanation: 3 negatives (odd), min_abs = 0 -> 1+0+1+2+1+3 - 2*0 = 8")
    
    # Example 4: All positive
    print("\n=== Example 4 ===")
    matrix = [[1, 2], [3, 4]]
    result = sol.maxMatrixSum(matrix)
    print(f"Input: {matrix}")
    print(f"Output: {result}")
    print(f"Expected: 10")
    print(f"Explanation: 0 negatives (even) -> sum of all = 10")
    
    # Example 5: All negative
    print("\n=== Example 5 ===")
    matrix = [[-1, -2], [-3, -4]]
    result = sol.maxMatrixSum(matrix)
    print(f"Input: {matrix}")
    print(f"Output: {result}")
    print(f"Expected: 8")
    print(f"Explanation: 4 negatives (even) -> can make all positive = 1+2+3+4 = 10")
    
    # Example 6: Single negative
    print("\n=== Example 6 ===")
    matrix = [[5, -3], [7, 2]]
    result = sol.maxMatrixSum(matrix)
    print(f"Input: {matrix}")
    print(f"Output: {result}")
    print(f"Expected: 13")
    print(f"Explanation: 1 negative (odd) -> 5+3+7+2 - 2*2 = 17 - 4 = 13")