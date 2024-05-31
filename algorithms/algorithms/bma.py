def bad_character_heuristic(pattern):
    """Creates the bad character heuristic table."""
    bad_char_table = {}
    for i in range(len(pattern) - 1):
        bad_char_table[pattern[i]] = len(pattern) - 1 - i
    return bad_char_table

def good_suffix_heuristic(pattern):
    """Creates the good suffix heuristic table."""
    m = len(pattern)
    good_suffix_table = [m] * m
    last_prefix_position = m

    for i in range(m - 1, -1, -1):
        if is_prefix(pattern, i + 1):
            last_prefix_position = i + 1
        good_suffix_table[m - 1 - i] = last_prefix_position - i + m - 1

    for i in range(m - 1):
        slen = suffix_length(pattern, i)
        good_suffix_table[slen] = m - 1 - i + slen

    return good_suffix_table

def is_prefix(pattern, p):
    """Checks if pattern[p:] is a prefix of pattern."""
    m = len(pattern)
    for i in range(p, m):
        if pattern[i] != pattern[i - p]:
            return False
    return True

def suffix_length(pattern, p):
    """Returns the maximum length of the substring ending at p that is also a suffix."""
    length = 0
    m = len(pattern)
    while p >= 0 and pattern[p] == pattern[m - 1 - length]:
        length += 1
        p -= 1
    return length

def boyer_moore_search(text, pattern):
    """Implements the Boyer-Moore algorithm to find the pattern in the text."""
    if len(pattern) == 0:
        return 0
    bad_char_table = bad_character_heuristic(pattern)
    good_suffix_table = good_suffix_heuristic(pattern)

    m = len(pattern)
    n = len(text)

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print(f"Pattern found at index {s}")
            s += good_suffix_table[0]
        else:
            bad_char_shift = bad_char_table.get(text[s + j], m)
            good_suffix_shift = good_suffix_table[j]
            s += max(bad_char_shift, good_suffix_shift)

# Example usage
text = "AABACAABABACAA"
pattern = "ABC"
boyer_moore_search(text, pattern)
