class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def dfs(x):
            if x in memo:
                return memo[x]
            memo[x] = dfs(x-1) + dfs(x-2)
            return memo[x]
        return dfs(n)