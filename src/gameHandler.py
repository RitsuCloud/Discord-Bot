from fileParsing import TextGame

def main():
  obj = TextGame()
  scene_content = obj.lineToHash()
  print(scene_content)

if __name__ == "__main__":
  main()

