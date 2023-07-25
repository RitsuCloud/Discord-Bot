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
class TextGame:
    Node = namedtuple('Node', ['scene_number', 'description', 'options', 'death'])

    def __init__(self):
        self.gameOver = True
        self.lines = []
        self.scene_content = {}

    #text file parsing into hashmap 
    def fileToLine(self):
        file_path = "text-game/simple.txt"

        with open(file_path, 'r') as file:
            # Step 2: Read the file contents into a variable
            file_contents = file.read()

        # Step 3: Parse the file contents 
        self.lines = file_contents.split("\n")  # Split the content into lines

    def lineToHash(self):
        i = 0
        scene_num = "0"
        description = ""
        option = []
        death_scene = False
        
        while i < len(self.lines) and self.lines[i] != "END":
            curLine = self.lines[i].split(" ")

            #if curLine is --- line for seperating scene, we skip it and reset the variables
            if curLine[0] == "---":
                # adds the node into the hash
                print(death_scene)
                self.scene_content[scene_num] = self.Node(scene_number=scene_num, description= description, 
                                                options=option, death=death_scene)
                scene_num = "0"
                description = ""
                option = []
                death = False
            
            #if curLine is the scene_number
            if curLine[0] == "scene_number:":
                scene_num = int(curLine[1])
            
            #if curLine is the description
            if curLine[0] == "description:":
                for k in range(1, len(curLine)):
                    description += curLine[k] + " "
                
            if curLine[0] == "option:":
                i += 0

            if curLine[0] == "DEATH:":
                death_scene = True
            
            i += 1

    #this part handles the user's input and game logic
    def startGame():
        return False

    def forMain(self):
        self.fileToLine()
        self.lineToHash()
        print(self.scene_content)   

def main():
  obj = TextGame()
  obj.forMain()
  
if __name__ == "__main__":
    main()