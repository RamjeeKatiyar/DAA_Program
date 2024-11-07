def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the dp table
    for length in range(2, n+1):  # length of the subsequence
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

# Example usage
s = "bbabcbcab"
print(longest_palindromic_subsequence(s)) 
