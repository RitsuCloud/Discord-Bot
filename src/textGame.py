# this file is where the game and file parsing will be at

def main():
  file_path = "text-game/example.txt"

  with open(file_path, 'r') as file:
      # Step 2: Read the file contents into a variable
      file_contents = file.read()

  # Step 3: Parse the file contents (Example: Printing each line)
  lines = file_contents.split("\n")  # Split the content into lines
  for line in lines:
      print(line)

if __name__ == "__main__":
    main()