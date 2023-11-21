def max_length_substring(N, S, Q, X, Y):
    # import pdb;pdb.set_trace()
    result = []

    for i in range(Q):
        X_i = X[i]
        Y_i = Y[i]

        # Update the character at index X[i]
        S = S[:X_i - 1] + Y_i + S[X_i:]

        # Calculate the maximum length of substring with the same characters
        max_length = 1
        current_length = 1

        for j in range(1, N):
            if S[j] == S[j - 1]:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1

        max_length = max(max_length, current_length)
        result.append(max_length)

    return result

# Example usage
N = 6
S = "ababcc"
Q = 3
X = [6,3,2]
Y = ['d','b','a']
result = max_length_substring(N, S, Q, X, Y)
print(result)


def solve(N, Tiles):
    dp = [[0] * N for _ in range(N)]

    for i in range(N):
        dp[i][i] = Tiles[i]

    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            dp[i][j] = max(Tiles[i] - dp[i + 1][j], Tiles[j] - dp[i][j - 1])

    return dp[0][N - 1]

# Input processing
N = int(input())
Tiles = [int(input()) for _ in range(N)]

# Call the solve function
result = solve(N, Tiles)

# Output the result
print(result)

