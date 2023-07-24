from collections import namedtuple
"""
Each block of the game will be in the form of
#1 number
description
options # with their corresponding number to jump to 

this will probably require a struct and hashmap
"""
#options should be a list, where list[0] is option1, etc
#and when creating the node it should be name Node #follow why the scene_number
Node = namedtuple('Node', ['scene_number', 'description', 'options', 'death'])

gameOver = True
lines = []
scene_content = {}

def main():
  fileToLine()
  Node1 = Node(scene_number=1, description="scene 1", options=[],death=False)
  Node1.options.append(("1",2))
  print(Node1.scene_number)
  print(Node1.description)
  print(Node1.options)

#text file parsing into hashmap 
def fileToLine():
    file_path = "text-game/simple.txt"

    with open(file_path, 'r') as file:
        # Step 2: Read the file contents into a variable
        file_contents = file.read()

    # Step 3: Parse the file contents 
    lines = file_contents.split("\n")  # Split the content into lines

def LineToHash():
    i = 0
    scene_num = "0"
    description = ""
    option = []
    death = False
    while lines[i] != "END":
        curLine = lines[i]

        #if curLine is --- line for seperating scene, we skip it
        if curLine[0] == "-":
            i += 1
            scene_num = "0"
            description = ""
            option = []
            death = False
            continue
        
        #if curLine is the scene_number
        if curLine[0] == "scene_number":
          return None
        
        #if curLine is the description
        if curLine[0] == "description":
            return None
            
        if curLine[0] == "option":
            return None

        if curLine[0] == "Death":
            return None
            
        i += 1
      

#this part handles the user's input and game logic
def startGame():
    return False

if __name__ == "__main__":
    main()