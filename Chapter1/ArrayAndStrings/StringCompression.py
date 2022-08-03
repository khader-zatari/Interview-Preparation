def string_comparession(s):
    res = []
    counter = 1
    for index in range(len(s) - 1):
        if s[index] != s[index + 1]:
            res.append(s[index] + str(counter))
            counter = 0
        counter += 1
    res.append(s[-1] + str(counter))

    return min(s, "".join(res), key=len)


print(string_comparession("aabbcc"))
