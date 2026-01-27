class Solution:
    def upper_bound(self,arr,target):
        result = len(arr)
        l = 0
        r = result - 1
        while l <= r:
            mid = (l + r ) // 2
            if arr[mid] > target:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result
    
    def upper_bound_rec(self,arr,target):
        def helper(l,r):
            if l > r:
                return l
            mid = (l+r) // 2
            if arr[mid] > target:
                return helper(l,mid-1)
            else:
                return helper(mid+1,r)
        return helper(0,len(arr)-1)

    
## Test Case
if __name__ == "__main__":
    arr = [2, 3, 7, 10, 11, 11, 25]
    target = 9
    sol = Solution()
    print(sol.upper_bound(arr, target))
    print(sol.upper_bound_rec(arr, target))