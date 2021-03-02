# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.

def CheckPermutation(t_one, t_two):
    if len(t_one) != len(t_two):
        print('Fail Length')
        return False
    if t_one == t_two:
        print('Fail same string')
        return False
    if set(t_one) != set(t_two):
        print('Fail set')
        return False
    if sorted(t_one) != sorted(t_two):
        print('Fail sort')
        return False
    return True


if __name__ == '__main__':
    print(CheckPermutation('apple', 'apples'))
    print(CheckPermutation('apple', 'apple'))
    print(CheckPermutation('apple', 'applo'))
    print(CheckPermutation('apale', 'eppla'))

    print(CheckPermutation('apple', 'aplpe'))