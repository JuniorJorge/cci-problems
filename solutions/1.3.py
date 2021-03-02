# URLify

def URLify(str, str_len):
    return str.lstrip().rstrip().replace(" ", "%20")

if __name__ == '__main__':
    print(URLify('Mr John Smith    ', 13))
