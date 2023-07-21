import gamba as gambaGame
import unittest

class GambaCase(unittest.TestCase):
    
    def testRegister(self):
      gambaGame.clear()

      res = gambaGame.register("Me")
      self.assertEqual(res, "Me is now registered! You have 1000 credits!")

      res2 = gambaGame.register("Me")
      self.assertEqual(res2, "Me have already registered!")

      res3 = gambaGame.register("Me")
      self.assertEqual(res2, "Me have already registered!")

if __name__ == "__main__":
    unittest.main()