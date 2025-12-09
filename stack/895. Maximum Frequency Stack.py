"""
===========================================================
895. Maximum Frequency Stack
===========================================================

🧩 Problem:
Design a stack-like data structure that supports the following operations:

1️⃣ `push(val)`  
   - Pushes an integer `val` onto the stack.

2️⃣ `pop()`  
   - Removes and returns the **most frequent** element in the stack.
   - If there is a tie for highest frequency, the element that was **pushed most recently** (i.e., closest to the top) is removed and returned.

🎯 Goal:
Implement the class `FreqStack`:

    class FreqStack:

        def __init__(self):
            pass

        def push(self, val: int) -> None:
            pass

        def pop(self) -> int:
            pass

-----------------------------------------------------------
Examples:
-----------------------------------------------------------

Example:
Input:
    ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
    [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]

Operations explanation:
    push(5)   → stack = [5]
    push(7)   → stack = [5,7]
    push(5)   → stack = [5,7,5]
    push(7)   → stack = [5,7,5,7]
    push(4)   → stack = [5,7,5,7,4]
    push(5)   → stack = [5,7,5,7,4,5]

Frequencies now:
    5 → 3 times
    7 → 2 times
    4 → 1 time

pop()   → returns 5   (5 has highest freq 3)
pop()   → next freq: 5 and 7 both have freq 2, but 7 is more recent → returns 7
pop()   → now 5 has freq 2, 7 has freq 1 → returns 5
pop()   → remaining max freq is 4 or 7 (both 1), but 4 is more recent → returns 4

Output:
    [null,null,null,null,null,null,null,5,7,5,4]

-----------------------------------------------------------
Intuition — Frequency + Stack of Stacks:
-----------------------------------------------------------

We need to support:
- **Most frequent** element → we need frequency counts.
- Tie-break by **most recent** among those → we need something stack-like for each frequency.

So we maintain two main structures:

1️⃣ `freq[val]` → how many times `val` has been pushed.
2️⃣ `group[f]` → a stack (list) of values that currently have frequency `f`
    - These stacks preserve **recency** among elements with the same frequency.

We also track:
3️⃣ `maxfreq` → the current highest frequency in the whole structure.

-----------------------------------------------------------
How `push(val)` works:
-----------------------------------------------------------

1. Increase its frequency:

       freq[val] += 1
       f = freq[val]

2. Update `maxfreq` if needed:

       maxfreq = max(maxfreq, f)

3. Push the value into the group corresponding to its new frequency:

       group[f].append(val)

So, all elements with the same frequency `f` are stored in `group[f]` in the order they achieved that frequency.  
The most recently pushed among them will be at the **end** of `group[f]`.

-----------------------------------------------------------
How `pop()` works:
-----------------------------------------------------------

We must:
- Remove and return the most frequent element.
- If tie, return the most recent among them.

Because:
- `maxfreq` stores the highest frequency.
- `group[maxfreq]` is a stack with *all* elements that currently have frequency `maxfreq`, ordered by recency.

Steps:

1. Pop from `group[maxfreq]`:

       val = group[maxfreq].pop()

   This gives the **most recent** value with frequency `maxfreq`.

2. Decrease its frequency:

       freq[val] -= 1

3. If `group[maxfreq]` becomes empty, reduce `maxfreq`:

       if not group[maxfreq]:
           maxfreq -= 1

4. Return `val`.

This directly satisfies the problem’s requirements.

-----------------------------------------------------------
Why This Works:
-----------------------------------------------------------

- `freq` tracks how often each value appears.
- `group[f]` acts like "layers" — each frequency has its own stack of values.
- `maxfreq` tells us which layer (frequency) to pop from.
- Thanks to the stack per frequency:
  - We automatically get the **most recent** value for that frequency.

All operations are **O(1)** average time.

-----------------------------------------------------------
⏱ Complexity:
-----------------------------------------------------------

- Time:
    - `push(val)`: O(1)
    - `pop()`:     O(1)
- Space:
    - O(n) to store frequencies and group stacks (where n is number of pushes).

-----------------------------------------------------------
Python Implementation (Freq Stack):
-----------------------------------------------------------
"""

from collections import defaultdict

class FreqStack:

    def __init__(self):
        # freq[val] = current frequency of val
        self.freq = defaultdict(int)
        # group[f] = stack (list) of values that have frequency f
        self.group = defaultdict(list)
        # current maximum frequency
        self.maxfreq = 0

    def push(self, val: int) -> None:
        # 1️⃣ Increase frequency
        f = self.freq[val] + 1
        self.freq[val] = f

        # 2️⃣ Update max frequency
        if f > self.maxfreq:
            self.maxfreq = f

        # 3️⃣ Push val into the corresponding frequency group
        self.group[f].append(val)

    def pop(self) -> int:
        # 1️⃣ Get the most recent element with max frequency
        val = self.group[self.maxfreq].pop()

        # 2️⃣ Decrease its frequency
        self.freq[val] -= 1

        # 3️⃣ If no more elements at this frequency, decrease maxfreq
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        # 4️⃣ Return the popped value
        return val


"""
-----------------------------------------------------------
Dry Run Example:
Input:
    ops  = ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
    args = [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]

-----------------------------------------------------------

Start:
    freq = {}
    group = {}
    maxfreq = 0

push(5):
    freq[5] = 1
    maxfreq = 1
    group[1] = [5]

push(7):
    freq[7] = 1
    group[1] = [5, 7]

push(5):
    freq[5] = 2
    maxfreq = 2
    group[2] = [5]

push(7):
    freq[7] = 2
    group[2] = [5, 7]

push(4):
    freq[4] = 1
    group[1] = [5, 7, 4]

push(5):
    freq[5] = 3
    maxfreq = 3
    group[3] = [5]

Now:
    freq = {5:3, 7:2, 4:1}
    group[1] = [5, 7, 4]
    group[2] = [5, 7]
    group[3] = [5]
    maxfreq = 3

pop():
    val = group[3].pop() → 5
    freq[5] = 2
    group[3] = []
    maxfreq → 2
    return 5

pop():
    val = group[2].pop() → 7   (stack [5, 7] → pop last)
    freq[7] = 1
    group[2] = [5]
    maxfreq stays 2
    return 7

pop():
    val = group[2].pop() → 5
    freq[5] = 1
    group[2] = []
    maxfreq → 1
    return 5

pop():
    val = group[1].pop() → 4   (stack [5, 7, 4])
    freq[4] = 0
    group[1] = [5, 7]
    maxfreq stays 1
    return 4

Outputs: [5, 7, 5, 4] ✅

-----------------------------------------------------------
"""

