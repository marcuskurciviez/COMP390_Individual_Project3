import util_funcs
import print_functions
import os
from lock_functions import lock
from unlock_functions import unlock

def help_command():
    """
    The help_command function is a series of calls to all the help print functions. Each print function is calling one of the various print messages
    in our print_functions file. With a call to the separation line following each one.
    """
    print_functions.print_separation_line('=', 50)
    print_functions.print_help_welcome()
    print_functions.print_separation_line('=', 50)
    print_functions.print_lock_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_unlock_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_msg_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_locked_help()
    print_functions.print_separation_line('=', 50)
    print_functions.print_clear_help()
    print_functions.print_separation_line('=', 50)

 def msg_command():
     # msg_command lists all the plain text files that are available if any.
    decrypted_file_list = [file for file in os.listdir() if file.endswith('_decrypted_msg.txt')]
    if len(decrypted_file_list) == 0:
        print('\n\tNo plaintext message files available.\n')
    else:
        print('\n\tPlaintext message files:\n')
        for file_name in decrypted_file_list:
            print_functions.print_msg_file_info(file_name)

    def locked_command():
        # locked_command shows all the encrypted files that are available, if any.
        encrypted_file_list = [file for file in os.listdir() if file.endswith('_encrypted_msg.txt')]
        if len(encrypted_file_list) == 0:
            print('\n\tNo encrypted message files available.\n')
        else:
            print('\n\tEncrypted message files:\n')
            for file_name in encrypted_file_list:
                print(f'\t{file_name}')
                print_functions.print_locked_file_info(file_name)

    def clear_command():
        # clear_command takes and gathers all the text files from the folder.
        lock_file_list = [file for file in os.listdir() if file.endswith('_lock.txt')]
        key_file_list = [file for file in os.listdir() if file.endswith('_key.txt')]
        encrypted_file_list = [file for file in os.listdir() if file.endswith('_encrypted_msg.txt')]
        decrypted_file_list = [file for file in os.listdir() if file.endswith('_decrypted_msg.txt')]
        master_text_file_list = lock_file_list + key_file_list + encrypted_file_list + decrypted_file_list
        for text_file in master_text_file_list:
            os.remove(text_file)

        print('\n\n\tAll \'lock\', \'key\', \'encrypted message\', and \'decrypted message\' text files removed.\n')


    def unlock_command(arg_list: list):
        target_encrypted_file: str = arg_list[2]
        file_list = os.listdir()
        if (target_encrypted_file in file_list) and (len(target_encrypted_file) == 22) and \
                (target_encrypted_file[-18:] == '_encrypted_msg.txt'):
            unlock(target_encrypted_file)
        else:
            print(f'\n\t{target_encrypted_file} does not exist or is invalid\n')

    def lock_command(arg_list: list):
        util_funcs.validate_lock_depth(arg_list[2])
        lock_file = util_funcs.generate_lock_file(arg_list[2])
        lock(arg_list[3], lock_file)

