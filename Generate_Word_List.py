
# Generate Password List Or Word List

import random
import string

def Generate_Word_List(line_, min_, max_, valu=''):
    List_Word = []
    for _ in range(line_):
        num_char = random.randint(min_, max_)
        char = ''.join(random.choice(string.ascii_lowercase) for i in range(num_char))
        position = random.randint(0, len(char))
        modified_char = char[:position] + valu + char[position:]
        List_Word.append(modified_char)
    for item in List_Word:
        print(item)
    return List_Word

def START():
    while True:
        print()
        num_lines = input(' - Enter number of lines or [D for default] exit(e): ').strip().lower()
        if num_lines == 'e':
            print()
            print('Exit, Bye')
            print()
            break
        elif num_lines == '':
            num_lines = 'd'

        print()
        min_chars = input(' - Enter minimum number of characters per line or [D for default] exit(e): ').strip().lower()
        if min_chars == 'e':
            print()
            print('Exit, Bye')
            print()
            break
        elif min_chars == '':
            min_chars = 'd'

        print() 
        max_chars = input(' - Enter maximum number of characters per line or [D for default] exit(e): ').strip().lower()
        if max_chars == 'e':
            print()
            print('Exit, Bye')
            print()
            break
        elif max_chars == '':
            max_chars = 'd'

        print()
        default_value = input('Enter a default value to append to each line [Y/N] exit(e): ').strip().lower()
        if default_value == 'e':
            print()
            print('Exit, Bye')
            print()
            break
        elif default_value == '':
            default_value = 'n'

        if num_lines == 'd':
            num_lines = 100
        elif num_lines.isdigit() and 0 < int(num_lines):
            num_lines = int(num_lines)
        else:
            print()
            print('Invalid input for number of lines')
            continue

        if min_chars == 'd':
            min_chars = 5
        elif min_chars.isdigit() and 0 < int(min_chars):
            min_chars = int(min_chars)
        else:
            print()
            print('Invalid input for minimum characters')
            continue

        if max_chars == 'd':
            max_chars = 10
        elif max_chars.isdigit() and 0 < int(max_chars):
            max_chars = int(max_chars)
        else:
            print()
            print('Invalid input for maximum characters')
            continue

        if min_chars > max_chars:
            print()
            print('Minimum characters cannot be greater than maximum characters')
            continue

        if default_value == 'y':
            print()
            default_val = input('Type:')
            Generate_Word_List(num_lines, min_chars, max_chars, default_val)
        else:
            Generate_Word_List(num_lines, min_chars, max_chars)

START()
