from collections import deque
import re

def is_palindrome(s):
    s = re.sub(r"\s+", "", s).lower()
    char_deque = deque(s)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


print("А роза упала на лапу Азора: ", is_palindrome("А роза упала на лапу Азора"))
print("Аргентина манит негра: ", is_palindrome("   Аргентина   манит негра"))
print("Не паліндром: ", is_palindrome("Не паліндром"))
print("12321: ", is_palindrome("12321"))