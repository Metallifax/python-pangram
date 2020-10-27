import string

def is_pangram(s):
    stringArr = []
    count = 0
    for i in range(26):
        stringArr.append(string.ascii_letters[i])

    for i in range(len(s)):
        if s[i] in stringArr:
            count += 1
            print(s[i])
            continue
        else:
            return False
    return True

    # if s in stringArr:
    #     return 'Bingo!'
    # else:
    #     print(stringArr)
    #     return 'Not a bingo.'

print(is_pangram('abcdefghijklmnopqrstuvwxyz'))

# 'abcdefghijklmnopqrstuvwxyz'