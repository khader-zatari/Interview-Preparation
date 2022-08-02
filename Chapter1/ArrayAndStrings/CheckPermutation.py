from collections import Counter


def check_permutation_sort(s1, s2):
    if(len(s1) != len(s2)):
        return False

    sort_s1, sort_s2 = sorted(s1), sorted(s2)

    for i in range(len(s1)):
        if sort_s1[i] != sort_s2[i]:
            return False

    return True


def check_permutation_count(s1, s2):
    if len(s1) != len(s2):
        return False

    arr = [0] * 256

    for char in s1:
        arr[ord(char)] += 1

    for char in s2:
        if(arr[ord(char)] == 0):
            return False

        arr[ord(char)] -= 1
    return True

def check_permutation_count_2(s1 , s2):
    if (len(s1) != len(s2)): 
        return False
    
    return Counter(s1) == Counter(s2)

example_true = ['dog', 'god', 'odg', 'gdo']
example_false = ['dog', 'doge', 'odge', 'gdo ']

for i in example_false:
    for j in example_false:
        print(check_permutation_sort(i, j))
