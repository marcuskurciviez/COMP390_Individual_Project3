import random
import string
import sys
import os


def generate_lock_file(size):
    # generate random lock file name: [random]_lock.txt
    lock_file_name = generate_unique_lock_file_name()
    try:
        return write_to_lock_file(lock_file_name, size)
    except Exception as file_error:
        print(f'\n\tAn error occurred while trying to write to {lock_file_name}:{file_error}\n')
        return None

def generate_unique_lock_file_name():
    """
    This function serves the purpose of generating a unique file name that doesn't exist. It should return a randomly generated
    XXXXX_lock.txt filename string.
    """
    timeout_counter = 0
    files_in_dir = os.listdir()
    while timeout_counter < 25:
        random_file_name = '_lock.txt'
        for _ in range(8):
            random_letter = random.choice(string.ascii_letters)
            random_file_name = random_letter + random_file_name
        if random_file_name not in files_in_dir:
            break
        timeout_counter = timeout_counter + 1

    return random_file_name

def write_lock_values_to_file(num_values: int, file_obj: typing.TextIO):
    # This function writes a series of numbers to the locked file that is encrypted.
    for line_ct in range(int(num_values)):
        rand_int1 = random.randint(0, sys.maxsize)
        if line_ct < int(num_values) - 1:
            print(f'{rand_int1}', file=file_obj)
            continue
        file_obj.write(f'{rand_int1}')

def write_to_lock_file(file_name, size_val):
    with open(file_name, 'w') as text_file:
        write_lock_values_to_file(size_val, text_file)
    return file_name

def lock_depth_positive_check(depth, arg_val):
    if depth <= 0:
        print(f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0 (zero).\n')
        return None
    return depth

def validate_lock_depth(arg_value: str):
    # checks to see if an int is passed
    try:
        lock_depth = int(arg_value)
        return lock_depth_positive_check(lock_depth, arg_value)
    except ValueError:
        print(f'\n\tInvalid lock depth: \'{arg_value}\'. Must be an integer greater than 0 (zero).\n')
        return None
