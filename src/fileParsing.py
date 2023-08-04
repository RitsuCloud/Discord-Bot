from collections import namedtuple

#options should be a list, where list[0] is option1, etc
#and when creating the node it should be name Node #follow why the scene_number
class TextGame:
    Node = namedtuple('Node', ['scene_number', 'description', 'options','contain', 'death'])

    def __init__(self, num):
        self.fileName = "text-game/adventure" + str(num) + ".txt"

    #text file parsing into lines
    def fileToLine(self):
        file_path = self.fileName

        with open(file_path, 'r') as file:
            # Step 2: Read the file contents into a variable
            file_contents = file.read()

        # Step 3: Parse the file contents 
        return file_contents.split("\n")  # Split the content into lines
    
    #lines parce into hashmap and namedtuple
    def lineToHash(self):
        i = 0
        scene_num = "0"
        description = ""
        option = {}
        contains = []
        death_scene = False
        
        lines = self.fileToLine()
        scene_content = {}

        while i < len(lines) and lines[i] != "END":
            curLine = lines[i].split(" ")
            
            if curLine[0] == "inventory:":
                scene_content["inventory"] = {}
                for k in range(1, len(curLine)):
                    scene_content["inventory"][curLine[k]] = False
                    print(curLine[k])
                    print(scene_content["inventory"][curLine[k]])

            #if curLine is --- line for seperating scene, we skip it and reset the variables
            if curLine[0] == "---":
                # adds the node into the hash
                scene_content[scene_num] = self.Node(scene_number=scene_num, description= description, 
                                                options=option, contain=contains, death=death_scene)
                scene_num = "0"
                description = ""
                option = {}
                contains = []
                death = False
            
            #if curLine is the scene_number
            if curLine[0] == "scene_number:":
                scene_num = int(curLine[1])
            
            #if curLine is the description
            if curLine[0] == "description:":
                for k in range(1, len(curLine)):
                    description += curLine[k] + " "

            #add what this scene contains
            if curLine[0] == "contain:":
                for k in range(1, len(curLine)):
                    contains.append(curLine[k])

            # options needs changing, since we can't just display only the description but also 
            # the options, and how the user pick the options is also another thing to consider
            if curLine[0] == "option:":
                #option be hashmap with key as "dirction" and value as the scene they go to
                option[curLine[1]] = int(curLine[2])

            if curLine[0] == "DEATH:":
                death_scene = True
            
            i += 1
        return scene_content