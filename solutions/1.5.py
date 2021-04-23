# One Away
def one_away(string_1, string_2):
    # One Character Removed from String 2
    if (len(string_1) - len(string_2)) == 1:
        for pos in range(len(string_1)):
            if string_1[pos] != string_2[pos]:
                if string_1[pos + 1:] == string_2[pos:]:
                    return True
                return False 
        return True
    # One Character Added
    elif (len(string_2) - len(string_1)) == 1:
        for pos in range(len(string_2)):
            if string_2[pos] != string_1[pos]:
                if string_2[pos + 1:] == string_1[pos:]:
                    return True
                return False 
        return True
    # Same Amount of Characters
    elif len(string_2) == len(string_1):
        if string_1 == string_2:
            return True
        for pos in range(len(string_2)):
            if string_1[pos] != string_2[pos]:
                if string_1[pos + 1:] == string_2[pos + 1:]:
                    return True
                return False 
        return True
    else:
        return False


if __name__ == '__main__':
    print(one_away("tast", "test"))
