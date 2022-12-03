import sys

import command_functions

import print_functions

"""The main file: jlock.py includes two functions: parse_command_line_args and jlock_main. The first function has been refactored to simple if else statements
where the first if will print out the welcome message. The first elif command prints out the help text, and inside that is a couple of if elif statements for
each of the help commands. From there the function goes into the various commands for the lock and unlock functions."""
def parse_command_line_args(arg_list: list):
    arg_list_len = len(arg_list)

    if arg_list_len == 1:
        print(print_functions.print_welcome_message)

    elif arg_list_len == 2:
        command = arg_list[1]
        if command == '-help' or command == '-h':
            command_functions.help_command()

        elif command == '-msg':
            command_functions.msg_command()

        elif command == '-locked':
            command_functions.locked_command()

        elif command == '-clear':
            command_functions.clear_command()

        else:
            print('Error: invalid command')

    elif arg_list_len == 3:
        if arg_list[1] == '-unlock':
            command_functions.unlock_command(arg_list)

        else:
            print('Error: invalid command')

    elif arg_list_len == 4:
        if arg_list[1] == '-lock':
            command_functions.lock(arg_list)

        else:
            print('Error: invalid command')

    else:
        print('Error: invalid command')


def jlock_main():
    # get command line arguments
    arg_list = sys.argv

    # check for empty string in command line args - empty strings are invalid input
    if '' in arg_list:
        print('Error: invalid command')
        return

    parse_command_line_args(arg_list)


if __name__ == '__main__':
    jlock_main()
