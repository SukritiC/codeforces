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

# BruteForce
if __name__ == "__main__":
    str1 = "ADOBECODEBANC"
    threat = "ABC"
    n = len(str1)
    th = []
    for element in threat:
        th.append(element)

    start_i = 0
    end_i = 0
    substr = ""
    len1 = int(1e9)
    for i in range(n):

        if str1[i] in th:
            th.remove(str1[i])
            print(th, "      ", i, "   ", len(th))
            if len(th) == 0:
                end_i = i
                print(end_i, "     ", start_i)
                if len1 > end_i - start_i + 1:
                    len1 = end_i - start_i + 1
                    substr = str1[start_i:end_i + 1]
                for element in threat:
                    th.append(element)

            elif len(th) == len(threat) - 1:
                start_i = i

    print(substr)

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
            while count == len(t): # this is suppose to execute when the
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