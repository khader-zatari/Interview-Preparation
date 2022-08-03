def palindrome_permutation(s):
    arr = [0] * (ord('z') - ord('a') + 1)
    odd = 0
    for i in s: 
        index = help(i)
        if index != -1:    
            arr[index] += 1
            if arr[index] % 2 == 1:
                odd += 1
            else:
                odd -= 1
    return odd <= 1

    

def help(char):
    if ord('A') <= ord(char) <= ord('Z'):
        return ord(char) - ord('A')

    elif ord('a') <= ord(char) <= ord('z'):
        return ord(char) - ord('a')
    
    else:
        return -1
print(palindrome_permutation("Tact Coaa"))