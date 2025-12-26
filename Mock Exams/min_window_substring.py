'''
Scenario:
    You are designing a security monitoring system for a high-frequency trading platform. The system generates a
    continuous stream of audit logs, represented as a single massive string S. Each character represents a specific
    event type.

    We have a specific "Threat Signature," represented by string T.

    We need to find the shortest continuous segment within the log stream S that contains all the
    events present in the Threat Signature T (including duplicates).

    If no such segment exists, return an empty string.

    Input:
    S = "ADOBECODEBANC" (The Log Stream)
    T = "ABC" (The Threat Signature)Output:"BANC" (The shortest substring containing 'A', 'B', and 'C').

    Constraints:
    Length of S up to 10^5.
    Efficiency is critical. Latency must be minimal.
'''

# Better Approach - Sliding Window

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minlen = float('inf')
        sIndex = -1
        hash = [0] * 256
        for char in t:
            hash[ord(char)] += 1

        count = 0
        l, r = 0, 0

        while r < len(s):
            if hash[ord(s[r])] > 0:
                count += 1
            hash[ord(s[r])] -= 1
            print("1", count,"   ",r,l,"  ",minlen)
            while count == len(t): # this is suppose to execute when all n characters if t are found
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    sIndex = l

                hash[ord(s[l])] += 1
                if hash[ord(s[l])] > 0:
                    count -= 1
                l += 1
                print("2",count,"   ",r,l,"  ",minlen)
            r += 1

        return s[sIndex:sIndex + minlen] if sIndex != -1 else ""


if __name__ == "__main__":
    str1 = "ADOBECODEBANC"
    threat = "ABC"

    s = Solution()
    print(s.minWindow(str1, threat))