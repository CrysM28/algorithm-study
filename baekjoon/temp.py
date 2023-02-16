
import sys

rev = {'A':'A', 'E': '3', 'H':'H', 'I':'I', 'J':'L', 'L': 'J', 
'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 
'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S', 
'3': 'E', '5': 'Z', '8': '8'}


lines = sys.stdin.readlines()

for line in lines:
    word = line.rstrip()

    is_palindrome = True
    is_mirror = False

    left = 0
    right = len(word)-1

    while left <= right:
        mirror_left, mirror_right = '', ''
        if word[left] in rev:
            mirror_left = rev[word[left]]
        if word[right] in rev:
            mirror_right = rev[word[right]]

        if word[left] == mirror_right or mirror_left == word[right]:
            is_mirror = True

        if word[left] != word[right]:
                is_palindrome = False
                break
        left += 1
        right -= 1

    print(is_palindrome, is_mirror)

    if is_palindrome:
        if is_mirror:
            print(word, "-- is a mirrored string.")
    else:
        print(word, "-- is not a palindrome.")