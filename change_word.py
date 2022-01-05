# Ucitati text
# Uneti rec koju zelimo zameniti
# Uneti rec zamene
# Novi tekst sacuvati u novom fajlu
# Stari fajl ostaje nepromenjen

def char_changer():
    base_char = input("Enter base char: ")
    enc_char = input("Enter new char: ")
    original_file_name = input("Enter the name of file: ")
    new_file_name = input("Enter the name of new file: ")
    with open(original_file_name) as source_file:
        lines = source_file.readlines()
    def input_char():
             with open(new_file_name, 'w') as output:
                 for line in lines:
                    new_line = line.replace(base_char, enc_char)
                    output.write(new_line)
    input_char()

char_changer()
