# https://leetcode.com/problems/string-compression-ii/

def main():

    sol = Solution()

    print(sol.getLengthOfOptimalCompression("aaabcccd", 2))

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        # 2d array
        dp = [[9999 for j in range(n + 1)] for i in range(n + 1)]

        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(k + 1):
                cnt = 0
                delete = 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        delete += 1
                    
                    # 'Greater' if a > 5 else 'Lesser'
                    if (j - delete) >= 0:
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - delete] + 1 + (3 if cnt >= 100 else 2 if cnt >= 10 else 1 if cnt >= 2 else 0))
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
        
        return dp[n][k]   

if __name__ == "__main__":
    main()