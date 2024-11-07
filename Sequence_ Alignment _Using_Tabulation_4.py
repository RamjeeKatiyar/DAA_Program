def sequence_alignment(seq1, seq2, match_score=1, gap_penalty=-1, mismatch_penalty=-1):
    m, n = len(seq1), len(seq2)
    
    # Create the dp table with base cases
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i * gap_penalty
    for j in range(n + 1):
        dp[0][j] = j * gap_penalty
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i-1] == seq2[j-1]:
                score = match_score
            else:
                score = mismatch_penalty
            
            dp[i][j] = max(
                dp[i-1][j-1] + score,  # Match or mismatch
                dp[i-1][j] + gap_penalty,  # Gap in seq2
                dp[i][j-1] + gap_penalty   # Gap in seq1
            )
    
       
    return dp[m][n]

# Example usage
seq1 = "AGCTG"
seq2 = "ACGT"
print(sequence_alignment(seq1, seq2))
