def kmp_partial_match_table(pattern):
    """Preprocess the pattern to create the partial match table."""
    length = len(pattern)
    partial_match_table = [0] * length
    j = 0  # length of previous longest prefix suffix

    # The loop calculates partial_match_table[i] for i from 1 to M-1
    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = partial_match_table[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
            partial_match_table[i] = j
        else:
            partial_match_table[i] = 0

    return partial_match_table

def kmp_search(text, pattern):
    """Search for the pattern in the text using the KMP algorithm."""
    partial_match_table = kmp_partial_match_table(pattern)
    m = len(pattern)
    n = len(text)
    i = 0  # index for text
    j = 0  # index for pattern

    result = []
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j)
            j = partial_match_table[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = partial_match_table[j - 1]
            else:
                i += 1

    return result

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = kmp_search(text, pattern)
print("Pattern found at indices:", result)

