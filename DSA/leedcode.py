def lengthOfLongestSubstring(s: str) -> int:
    """
    Finds the length of the longest substring without duplicate characters.
    """
    charMap = {}
    maxLength = 0
    start = 0
    
    

    for end in range(len(s)):
        # If the current character is a duplicate within the current window
        if s[end] in charMap and charMap[s[end]] >= start:
            # Move the start of the window
            start = charMap[s[end]] + 1

        # Update the last seen index of the current character
        charMap[s[end]] = end

        # Calculate the length of the current substring and update max length
        currentLength = end - start + 1
        maxLength = max(maxLength, currentLength)

    return maxLength

# Example usage
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3 (for "abc")
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1 (for "b")
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3 (for "wke")
print(lengthOfLongestSubstring(""))          # Output: 0
