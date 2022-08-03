from numpy import str_


def urlify_replace(s, str_len):
    return s[:str_len].replace(" ", "%20")


def urlify(s, str_len):
    char_list = list(s)
    char_list_len = len(char_list)

    for index in reversed(range(str_len)):
        if char_list[index] == ' ':

            char_list[char_list_len - 3: char_list_len] = "%20"
            char_list_len -= 3 

        else:
            char_list[char_list_len - 1] = char_list[index]
            char_list_len -= 1

    return "".join(char_list[char_list_len:])


print(urlify("much ado about nothing      ", 22))
