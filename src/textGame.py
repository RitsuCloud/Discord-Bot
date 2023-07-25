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
  #LineToHash()
  print(scene_content)


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
        curLine = lines[i].split(" ")

        #if curLine is --- line for seperating scene, we skip it and reset the variables
        if curLine[0] == "---":
            # adds the node into the hash
            scene_content[scene_num] = Node(scene_number=scene_num, description= description, 
                                            options=option, death=death)

            i += 1
            scene_num = "0"
            description = ""
            option = []
            death = False
            continue
        
        #if curLine is the scene_number
        if curLine[0] == "scene_number:":
          scene_num = int(curLine[1])
        
        #if curLine is the description
        if curLine[0] == "description:":
            for i in range(1, len(curLine)):
                description += curLine[i]
            
        if curLine[0] == "option:":
            return None

        if curLine[0] == "Death:":
            death = True
            
        i += 1
      

#this part handles the user's input and game logic
def startGame():
    return False

if __name__ == "__main__":
    startGame()