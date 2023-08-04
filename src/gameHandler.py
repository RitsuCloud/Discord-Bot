from fileParsing import TextGame

scene_content = {}
gameOver = True
cur_scene = 1


def parse(num):
  global scene_content

  obj = TextGame(num)
  scenes = obj.lineToHash()
  for num in scenes.keys():
    scene_content[num] = scenes[num]
    
def startGame(num):
  global gameOver
  global cur_scene
  gameOver = False
  cur_scene = 1
  parse(num)
  res = parseDiscription(cur_scene)
  return res

#maybe we need some kind of option recieve thing 
def optionPick(direction):
  global scene_content
  global gameOver
  global cur_scene
  
  if gameOver:
    return "Game is over/not started, use !adventure to start over!"
  
  if not direction in scene_content[cur_scene].options:
    return "Not Valid Input, please only input the direction you wish to continue."
  
  if scene_content[cur_scene].death:
    gameOver = True
  cur_scene = scene_content[cur_scene].options[direction]
  res = parseDiscription(cur_scene)
  return res

def parseDiscription(num):
  global scene_content

  res = f'{scene_content[num].description} \n'
  if scene_content[num].options:
    for key in scene_content[num].options.keys():
      if scene_content["inventory"] and key in scene_content["inventory"]:
        scene_content["inventory"][key] = True
      else:
        res += f'Option: {key} \n'
  return res

if __name__ == "__main__":
  startGame(2)



