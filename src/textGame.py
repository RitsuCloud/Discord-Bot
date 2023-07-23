"""
Each block of the game will be in the form of
#1 number
description
options # with their corresponding number to jump to 

this will probably require a struct and hashmap
"""

lines = []

def main():
  text_parsing("")

def text_parsing(num):
    file_path = "text-game/example.txt" + num

    with open(file_path, 'r') as file:
        # Step 2: Read the file contents into a variable
        file_contents = file.read()

    # Step 3: Parse the file contents (Example: Printing each line)
    lines = file_contents.split("\n")  # Split the content into lines
    for line in lines:
        if not line[0] == "-":
            print(line)

if __name__ == "__main__":
    main()