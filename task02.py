from collections import deque
from colorama import Back


def is_palindrome(input_string: str) -> bool:
    cleaned_string = ''.join(
        char.lower() for char in input_string if char.isalnum()
    )
    char_deque = deque(cleaned_string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


input_str = "A man a plan a canal Panama"
# input_str = "Able was I ere` I saw Elba"
# input_str = "Hello, World!"`

if is_palindrome(input_str):
    print(Back.GREEN + f'"{input_str}" є паліндромом.')
else:
    print(Back.RED + f'"{input_str}" не є паліндромом.')
