# Is Unique
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def isUnique(text_string):
    if(len(set(text_string)) == len(text_string)):
        return True
    return False

# Sort string approach
def isUniqueNoDS(text_string):
    sorted_string = sorted(text_string)
    print(sorted_string)
    for index, char in enumerate(sorted_string):
        if index == 0:
            next
        if char == sorted_string[index - 1]:
            return False
    return True

# Create your own hash map approach

if __name__ == "__main__":
    print(isUniqueNoDS('mango'))
    print(isUniqueNoDS('apple'))