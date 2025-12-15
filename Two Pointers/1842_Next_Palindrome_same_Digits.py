

# ------------------------------------------------------------
# 1842 Next Palindrome Using Same Digits
#
# Problem:
#   Given a palindromic numeric string num_str, produce the next
#   lexicographically larger palindrome that uses exactly the same
#   multiset of digits (reordering only). If none exists, return "".
#
# Assumption:
#   num_str is already a palindrome.
#
# Algorithm (Next Permutation of First Half + Mirror):
#   1) Validate palindrome (optional): If not palindrome, return "".
#   2) Take the first half fh = num_str[:n//2] as a list.
#   3) Compute next permutation of fh in-place:
#        - Find pivot i (rightmost index where fh[i] < fh[i+1]).
#        - If no pivot: fh is non-increasing -> no next -> return "".
#        - Find rightmost j where fh[j] > fh[i], swap fh[i], fh[j].
#        - Reverse suffix fh[i+1:].
#   4) Rebuild palindrome:
#        - Even length: fh + reversed(fh)
#        - Odd length:  fh + middle_digit + reversed(fh)
#
# Time:  O(n)
# Space: O(n) for output string
#
# Logic Hint:
#   Take the first half, find its next lexicographic permutation, then mirror it.
#   If the first half is already the largest (non-increasing), no higher palindrome exists.
#   For odd length, keep the middle digit unchanged.
# ------------------------------------------------------------

def find_next_palindrome(num_str):
    # Optional: enforce the palindrome assumption
    if num_str != num_str[::-1]:
        return ""  # Input must be palindromic for this approach

    def getPermutation(nums):
        n = len(nums)
        i = n - 2
        # 1) Find pivot: first index from right with nums[i] < nums[i+1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return False  # No next permutation

        # 2) Find rightmost successor greater than nums[i]
        j = n - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1

        # 3) Swap pivot and successor
        nums[i], nums[j] = nums[j], nums[i]

        # 4) Reverse the suffix
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return True

    n = len(num_str)
    mid = n // 2
    fh = list(num_str[:mid])  # first half as list for in-place permutation

    # Get next permutation of the first half
    if not getPermutation(fh):
        return ""  # No larger palindrome using the same digits

    # Rebuild palindrome by mirroring the new first half
    if n % 2 == 0:
        return "".join(fh) + "".join(reversed(fh))
    else:
        return "".join(fh) + num_str[mid] + "".join(reversed(fh))


# ------------------------------------------------------------
# Driver Tests
# ------------------------------------------------------------
def run_tests():
    cases = [
        # Even-length palindromes
        ("123321", "132231"),
        ("4554", "5445"),
        ("543345", ""),  # first half "543" has no next permutation

        # Odd-length palindromes
        ("14241", "41214"),
        ("32123", "32323"),
        ("9876789", ""),  # first half "9876" has no next permutation

        # Non-palindromic inputs (by design we return "")
        ("120345", ""),
        ("0012300", ""),  # not palindrome -> ""
    ]

    for s, expected in cases:
        out = find_next_palindrome(s)
        print(f"Input:    {s}")
        print(f"Output:   {out}")
        print(f"Expected: {expected}")

if __name__ == "__main__":
    run_tests()