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
  res = f'{scene_content[cur_scene].description} \n'
  for key in scene_content[cur_scene].options.keys():
    res += f'{key} \n'
  return res

if __name__ == "__main__":
  startGame()



