# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.

def CheckPermutation(t_one, t_two):
    if len(t_one) != len(t_two):
        return False
    if t_one == t_two:
        return False
    if set(t_one) != set(t_two):
        return False
    if sorted(t_one) != sorted(t_two):
        return False
    return True


if __name__ == '__main__':
    print(CheckPermutation('apple', 'aplpe'))
    print(CheckPermutation('apple', 'alape'))