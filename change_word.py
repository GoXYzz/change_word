# Take the original file and make another one with changed sequences of chars

# Symbol to change
base_char = input("Enter base char: ")
# New symbol
new_char = input("Enter new char: ")
# Name of file with original text
original_file_name = input("Enter the name of file: ")
# New file with changed text
new_file_name = input("Enter the name of new file: ")

class SymbolChanger():
    def __init__(self, base_char, new_char, original_file_name, new_file_name):
        self.base_char = base_char
        self.new_char = new_char
        self.original_file_name = original_file_name
        self.new_file_name = new_file_name

    def char_changer(self):
        # Load orignal file
        with open(original_file_name) as source_file:
            lines = source_file.readlines()
            # New file with changed text
            with open(new_file_name, 'w') as output:
                for line in lines:
                    new_line = line.replace(base_char, new_char)
                    output.write(new_line)

new_SymbolChanger = SymbolChanger(base_char, new_char, original_file_name, new_file_name)
new_SymbolChanger.char_changer()
