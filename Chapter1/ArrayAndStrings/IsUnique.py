def is_unique(s):
    if len(s) > 128:
        return False

    charArr = [False for i in range(128)]
    for char in s:
        res = ord(char)
        if charArr[res]:
            return False
        charArr[res] = True
    return True


def is_unique_bitWise_vector(s):
    if len(s) > 128:
        return False

    arr_num = 0
    for char in s:
        res = ord(char)
        

        if (arr_num & 1 << res) > 0:
            return False

        arr_num |= 1 << res

    return True

def is_unique_dic(s):
    
    char_dic = {}
    
    for char in s:
        if char in char_dic:
            return False
        char_dic[char] = 1

    return True




for example in ["abcde", "abcdee" , "afd=", "afd=="]:
    print(is_unique_dic(example))


