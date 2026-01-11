"""
===========================================================
636. Exclusive Time of Functions
===========================================================

🧩 Problem:
You are given:
    • An integer n → number of functions (IDs: 0 to n-1)
    • A list of logs, where each log is of the form:
          "function_id:start|end:timestamp"

Each function may call other functions, forming a call stack.

Rules:
1. A function can be called multiple times.
2. Logs are in chronological order.
3. When a function starts, it may pause the currently running function.
4. End timestamps are **inclusive**.

🎯 Goal:
Return an array where result[i] is the **exclusive execution time**
of function i.

Use a **stack-based simulation** of function calls.

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example 1:
Input:
n = 2
logs = [
    "0:start:0",
    "1:start:2",
    "1:end:5",
    "0:end:6"
]

Output:
[3, 4]

Explanation:
Function 0 runs at times: [0–1] and [6] → total 3  
Function 1 runs at times: [2–5] → total 4

-----------------------------------------------------------
Algorithm — Stack + prev_time:
-----------------------------------------------------------

Core idea:
Simulate the call stack of functions and track time gaps.

Key Insight:
• When a function STARTS → pause the previous function
• When a function ENDS   → consume inclusive time (+1)

Steps:
1. Initialize:
       stack = []              # stores function IDs
       result = [0] * n        # exclusive times
       prev_time = 0           # last processed timestamp

2. For each log:
       Parse: fid, op, time

3. If op == "start":
       - If stack is not empty:
             result[stack[-1]] += time - prev_time
       - Push fid onto stack
       - Set prev_time = time

4. If op == "end":
       - Pop function from stack
       - result[fid] += time - prev_time + 1
       - Set prev_time = time + 1

5. Return result

Why +1 on end?
End timestamps are **inclusive**.

-----------------------------------------------------------
⏱ Time & Space Complexity:
-----------------------------------------------------------

- Time Complexity:   O(L)
      where L = number of logs

- Space Complexity:  O(n)
      stack depth ≤ number of functions

-----------------------------------------------------------
"""
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        result = [0] * n
        prev_time = 0

        for log in logs:
            fid, op, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if op == "start":
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:  # end
                stack.pop()
                result[fid] += time - prev_time + 1
                prev_time = time + 1

        return result


#------------------------------------
# Driver Tests
#------------------------------------

sol = Solution()

print(sol.exclusiveTime(
    2,
    ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
))  # [3, 4]

print(sol.exclusiveTime(
    1,
    ["0:start:0", "0:end:0"]
))  # [1]

print(sol.exclusiveTime(
    2,
    ["0:start:0", "0:start:2", "0:end:5", "0:end:6"]
))  # [7]
