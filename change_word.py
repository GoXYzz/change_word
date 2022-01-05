def char_changer():
    # Word we want to change
    base_char = input("Enter base char: ")
    # New word
    enc_char = input("Enter new char: ")
    # Name of file with original text
    original_file_name = input("Enter the name of file: ")
    # New file with changed text
    new_file_name = input("Enter the name of new file: ")
    # Load orignal file
    with open(original_file_name) as source_file:
        lines = source_file.readlines()
        # New file with changed text
        with open(new_file_name, 'w') as output:
            for line in lines:
                new_line = line.replace(base_char, enc_char)
                output.write(new_line)


char_changer()
