
# Perfect To Programm Generate wordlist

import random
import string
import time

def Generate_Word_List(line_, min_, max_, valu=''):
    List_Word = []
    for _ in range(line_):
        num_char = random.randint(min_, max_)
        char = ''.join(random.choice(string.ascii_lowercase) for i in range(num_char))
        position = random.randint(0, len(char))
        modified_char = char[:position] + valu + char[position:]
        List_Word.append(modified_char)
    return List_Word

def Write_To_File(word_list, file_name='output.txt'):
    with open(file_name, 'w') as file:
        for word in word_list:
            file.write(word + '\n')
    print(f'Results have been written to {file_name}')

def Estimate_Time(num_lines, min_chars, max_chars):
    average_time_per_word = 0.0001 
    average_chars = (min_chars + max_chars) / 2
    total_time = num_lines * average_chars * average_time_per_word
    return total_time

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
        elif max_chars.isdigit() and 0 < int(max(max_chars)):
            max_chars = int(max_chars)
        else:
            print()
            print('Invalid input for maximum characters')
            continue

        if min_chars > max_chars:
            print()
            print('Minimum characters cannot be greater than maximum characters')
            continue

 
        estimated_time = Estimate_Time(num_lines, min_chars, max_chars)
        print(f'Estimated time to complete: {estimated_time:.2f} seconds')

        start_time = time.time() 

        if default_value == 'y':
            default_val = input('Type:')
            word_list = Generate_Word_List(num_lines, min_chars, max_chars, default_val)
        else:
            word_list = Generate_Word_List(num_lines, min_chars, max_chars)

        end_time = time.time()
        execution_time = end_time - start_time 

    
        Write_To_File(word_list)

        print(f'Time taken to generate word list: {execution_time:.2f} seconds')

START()
