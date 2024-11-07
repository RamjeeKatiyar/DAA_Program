def weighted_interval_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])  # Sort jobs by finish time
    n = len(jobs)

    # dp[i] is the maximum weight of non-overlapping jobs up to i
    dp = [0] * n

    def find_last_non_conflicting(i):
        # Binary search to find the last job that doesn't overlap with job i
        left, right = 0, i-1
        while left <= right:
            mid = (left + right) // 2
            if jobs[mid][1] <= jobs[i][0]:
                if jobs[mid+1][1] <= jobs[i][0]:
                    left = mid + 1
                else:
                    return mid
            else:
                right = mid - 1
        return -1

    dp[0] = jobs[0][2]  # The weight of the first job
    for i in range(1, n):
        # Find the last non-conflicting job
        last_non_conflict = find_last_non_conflicting(i)
        include_current = jobs[i][2] + (dp[last_non_conflict] if last_non_conflict != -1 else 0)
        dp[i] = max(dp[i-1], include_current)

    return dp[-1]

# Example usage
jobs = [(1, 3, 50), (3, 5, 20), (6, 9, 100), (2, 6, 70)]
print(weighted_interval_scheduling(jobs))  
