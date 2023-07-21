import gamba as gambaGame
import unittest

class GambaCase(unittest.TestCase):
    
    def test_register(self):
      gambaGame.clearData()
      res = gambaGame.register("Me")
      self.assertEqual(res, "Me is now registered! You have 1000 credits!")

      res = gambaGame.register("Me")
      self.assertEqual(res, "Me have already registered!")

      res = gambaGame.register("Me")
      self.assertEqual(res, "Me have already registered!")

    def test_check(self):
       gambaGame.clearData()
       res = gambaGame.check("Me")
       self.assertEqual(res, "Me has not been registered!")

       res = gambaGame.check("Me2")
       self.assertEqual(res, "Me2 has not been registered!")

       gambaGame.register("Me2")
       res = gambaGame.check("Me2")
       self.assertEqual(res, "Me2 has 1000 credits!")

    def test_clearData(self):
       gambaGame.clearData()
       res = gambaGame.check("Me2")
       self.assertEqual(res, "Me2 has not been registered!")

    def test_gamba(self):
       gambaGame.clearData()
       
       gambaGame.register("Me")
       res = gambaGame.gamba("Me", 1000)
       if "won" in res:
          self.assertEqual(res, "Me won!, now you have 2000 credits!")
       else:
          self.assertEqual(res, "Me lost! and you a brokie now, now you have 0 credits!")
      
       gambaGame.clearData()
       gambaGame.register("Me")
       res = gambaGame.gamba("Me", 1001)
       self.assertEqual(res, "Me dont have enough credits!")

if __name__ == "__main__":
    unittest.main()