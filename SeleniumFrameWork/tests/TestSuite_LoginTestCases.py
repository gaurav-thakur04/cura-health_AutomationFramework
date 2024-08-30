# 1. import the files
import unittest
from SeleniumFrameWork.tests.test_Login import LogInTest
from SeleniumFrameWork.tests.test_LoginDDT import Test_DDT_Login

# 2. Create the object of the class using UnitTest
lt = unittest.TestLoader().loadTestsFromTestCase(LogInTest)
lddt = unittest.TestLoader().loadTestsFromTestCase(Test_DDT_Login)


# 3. Test Suite
loginTestSuite = unittest.TestSuite([lt,lddt])


# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(loginTestSuite)

# Note : All the methods in test file should define in proper run order

