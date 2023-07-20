class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Define the dfs function with memoization
        def dfs(n, memo):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in memo:
                return memo[n]

            # Calculate the result for n and store it in the memo dictionary
            memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo)
            return memo[n]

        # Call the dfs function with an empty memo dictionary
        return dfs(n, {})
