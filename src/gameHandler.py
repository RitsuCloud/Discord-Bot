from fileParsing import TextGame

scene_content = {}
gameOver = False
cur_scene = 1

def parse():
  obj = TextGame()
  scenes = obj.lineToHash()
  for num in scenes.keys():
    scene_content[num] = scenes[num]
    
def startGame():
  parse()
  return scene_content[cur_scene].description

if __name__ == "__main__":
  startGame()



