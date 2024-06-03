# Naive algorithm for building suffix array of a given text
import sys
 
 
class Suffix:
    def __init__(self, index, suff):
        self.index = index
        self.suff = suff
 
# A comparison function used by sort() to compare two suffixes
def cmp(a, b):
    return (a.suff < b.suff) - (a.suff > b.suff)
 
# This is the main function that takes a string 'txt' of size n as an
# argument, builds and return the suffix array for the given string
def build_suffix_array(txt, n):
    # A structure to store suffixes and their indexes
    suffixes = [Suffix(i, txt[i:]) for i in range(n)]
 
    # Sort the suffixes using the comparison function
    # defined above.
    suffixes.sort(key=cmp)
 
    # Store indexes of all sorted suffixes in the suffix array
    suffix_arr = [suffixes[i].index for i in range(n)]
 
    # Return the suffix array
    return suffix_arr
 
# A utility function to print an array of given size
def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
# Driver program to test above functions
def main():
    txt = "banana"
    n = len(txt)
    suffix_arr = build_suffix_array(txt, n)
    print("Following is suffix array for", txt)
    print_arr(suffix_arr)
 
if __name__ == "__main__":
    main()
