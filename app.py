import os, time # imported needed modules

def time_delay(x): # Basic time delay function.
    time.sleep(x)

def welcome_screen(): # Welcomes the user. Only used when program is 1st opened.
    print('Welcome To VLC Absolute to Relative Path Modifier\n'
          '          Created By: Dr-Script\n'
          '                v12.30.16\n')
    time_delay(1)
    print('To Begin:')
    menu()

def menu(): # Main menu for program. This will allow the program to loop.
    time_delay(.5)
    print('Choose 1 for Instructions')
    time_delay(.5)
    print('Choose 2 to See Current Directory')
    time_delay(.5)
    print('Choose 3 to Run')
    user_input = input('Choice:')

    if user_input == '1':
        instructions()

    elif user_input == '2':
        current_directory()

    elif user_input == '3':
        replaced_playlist()

    else:
        print('Incorrect selection. Try again\n')
        time_delay(1)
        menu()

# Instructions def so user knows how to use program
def instructions():
    print('\n1. Make sure "app.py" is in the same folder as your playlist and files.\n'
          '  Quit and place "app.py" in same folder, then restart.\n'
          '\n'
          '2. Make sure your playlist is saved as "playlist.xspf and is saved to the same folder as your files and "app.py"\n'
          '\n'
          '3. IMPORTANT: All files must be in the same folder!\n'
          '   FOR BEST RESULTS: Create "playlist" on your desktop\n'
          '\n'
          '4. Once program states "Process Completed", "new_playlist.xspf" is the updated playlist.\n'
          'The old playlist remains unchanged as a safety measure.\n'
          '\n'
          '5. Make sure there are no spaces in your file names or directories to your current path.\n'
          '   Check be selecting option 2 in menu.'
          '\n'
          'Any questions, email: *********@gmail.com\n'
          '\n'
          'Press "ENTER" when ready to proceed.')
    instructions_input = input()
    menu()

def current_directory():
    working_directory = os.getcwd()
    modified_working_directory = working_directory.replace('\\', '/')
    file_directory = modified_working_directory + '/'
    print('\nCurrent Working File Directory:', file_directory, ''
                                                               '\nMake sure there are no spaces in your file path!', '\n')
    menu()

def replaced_playlist():
    try:
        file_playlist = open('playlist.xspf')
        content = file_playlist.read()
        message = content
        print('\nCurrent Playlist File:\n',message)
        working_directory = os.getcwd()
        modified_working_directory = working_directory.replace('\\', '/')
        file_directory = modified_working_directory + '/'
        print('\nCurrent File Directory:', file_directory, '\n')

        updated_playlist = message.replace(file_directory, '')
        print('New Playlist File:\n', updated_playlist)

        new_playlist = open('new_playlist.xspf', 'w')
        new_playlist.write(updated_playlist)
        print('\nSuccess! new_playlist.xspf saved.')
        new_playlist.close()
        file_playlist.close()
        print('\nProcess completed. Please exit "app.py"')

    except:
        print('"playlist.xspf" does not exist. Make sure "playlist.xspf" is in\n'
              'the same folder as all the media and Python program')
        print('Once "playlist.xspf" is in the same folder as playlist and media, select 2 again.\n')
        menu()

welcome_screen()
