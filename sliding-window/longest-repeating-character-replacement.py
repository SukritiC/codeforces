class Solution:
    """
    Function to find the longest substring
    with at most k characters replaced
    """

    def characterReplacement(self, s: str, k: int) -> int:

        """ Variable to store the maximum
        length of substring found"""
        maxLen = 0

        """ Variable to track the maximum frequency
        of any single character in the current window"""
        maxFreq = 0

        # Pointers to maintain the current window [l, r]
        l = 0
        r = 0

        # Hash array to count frequencies of characters
        hash = [0] * 26

        # Iterate through each starting point of substring
        while r < len(s):

            """ Update frequency of current
            character in the hash array"""
            hash[ord(s[r]) - ord('A')] += 1

            # Update max frequency encountered
            maxFreq = max(maxFreq, hash[ord(s[r]) - ord('A')])

            # Check if current window is invalid
            if (r - l + 1) - maxFreq > k:
                """ Slide the left pointer to
                make the window valid again"""
                hash[ord(s[l]) - ord('A')] -= 1

                # Move left pointer forward
                l += 1

            """ Update maxLen with the length
            of the current valid substring"""
            maxLen = max(maxLen, r - l + 1)

            # Move right pointer forward to expand window
            r += 1

        """ Return the maximum length of substring
        with at most k characters replaced"""
        return maxLen


if __name__ == "__main__":
    s = "AABABBA"
    k = 2

    # Create an instance of Solution class
    sol = Solution()

    length = sol.characterReplacement(s, k)

    # Print the result
    print(f"Maximum length of substring with at most {k} characters replaced: {length}")
