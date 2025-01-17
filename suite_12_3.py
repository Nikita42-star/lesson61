import unittest
import module_12_1
import module_12_2


MyTest_ST = unittest.TestSuite()
MyTest_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
MyTest_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(MyTest_ST)

