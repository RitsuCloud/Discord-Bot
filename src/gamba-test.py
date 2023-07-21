import gamba as gambaGame
import unittest

class GambaCase(unittest.TestCase):
    
    def testRegister(self):
      gambaGame.clear()

      res = gambaGame.register("Me")
      self.assertEqual(res, "Me is now registered! You have 1000 credits!")

      res = gambaGame.register("Me")
      self.assertEqual(res, "Me have already registered!")

      res = gambaGame.register("Me")
      self.assertEqual(res, "Me have already registered!")

    def testCheck(self):
       res = gambaGame.check("Me")
       self.assertEqual(res, "Me has not been registered!")

       res = gambaGame.check("Me2")
       self.assertEqual(res, "Me2 has not been registered!")

       gambaGame.register("Me2")
       res = gambaGame.check("Me2")
       self.assertEqual(res, "Me2 has 1000 credits!")

if __name__ == "__main__":
    unittest.main()