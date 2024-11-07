def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n

    # Compute the length of LIS ending at each element
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(arr)) 
