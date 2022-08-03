def check_one_operation(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        return check_replacement(s1, s2)

    elif len(s1) >= len(s2):
        return check_insertion(s1, s2)

    else:
        return check_insertion(s2, s1)


def check_insertion(s1, s2):

    edited = False
    i, j = 0, 0

    while i < len(s1) and j < len(s2):

        if s1[i] != s2[j]:
            if edited:
                return False

            i += 1
            edited = True
        else:
            i += 1
            j += 1
    return True


def check_replacement(s1, s2):
    edited = False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if edited:
                return False
            edited = True
    return True
    pass


print(check_one_operation("pale" , "ple"))