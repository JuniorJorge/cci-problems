# Palindrome Permutation

def isPalindromePermutation(str):
    # Remove all whitespace
    s = "".join(str.split())

    # Remove all duplicates
    str_set = set(s)

    # Create dictionary hash
    str_dict = {}
    for char in str_set:
        str_dict[char] = 0

    # Iterate through original stripped string
    # adding counts to the dict.
    for char in s:
        str_dict[char] += 1
    
    # A Palindrome can only contain one odd number set of char
    odd_num_flag = False
    for k, v in str_dict.items():
        if v % 2 != 0:
            if odd_num_flag is False:
                odd_num_flag = True
            else:
                return False
    return True

if __name__ == '__main__':
    print(isPalindromePermutation("abcbfcca"))
