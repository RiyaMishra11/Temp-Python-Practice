# File 61: Testing and Logging
# 11 practice programs

import logging,unittest,time
from io import StringIO
logging.basicConfig(level=logging.INFO,format="%(levelname)s: %(message)s")

# 1 Basic logging
logging.info("1 Logging started")

# 2 Simple function
def add(a,b):return a+b
print("2.",add(10,5))

# 3 Validation and exception
def divide(a,b):
    if b==0:raise ValueError("Cannot divide by zero")
    return a/b
print("3.",divide(10,2))

# 4 Assertion
assert add(2,3)==5
print("4. Assertion passed")

# 5 List assertion
x=[1,2,3];x.append(4)
assert x==[1,2,3,4]
print("5. List test passed")

# 6 Exception test
try:divide(10,0)
except ValueError as e:print("6.",e)

# 7 unittest
class MathTests(unittest.TestCase):
    def test_add(self):self.assertEqual(add(2,4),6)
    def test_divide(self):self.assertEqual(divide(8,2),4)
result=unittest.TextTestRunner(verbosity=0).run(
    unittest.TestLoader().loadTestsFromTestCase(MathTests))
print("7.",result.wasSuccessful())

# 8 Capture log output
stream=StringIO()
handler=logging.StreamHandler(stream)
logger=logging.getLogger("practice")
logger.addHandler(handler);logger.info("hello");handler.flush()
print("8.",stream.getvalue().strip());logger.removeHandler(handler)

# 9 Log exception
try:10/0
except ZeroDivisionError:logging.exception("9 Division error")

# 10 Palindrome test helper
def palindrome(s):
    s="".join(c.lower() for c in s if c.isalnum())
    return s==s[::-1]
assert palindrome("Madam") and not palindrome("Python")
print("10. Helper test passed")

# 11 Timing
start=time.perf_counter()
sum(range(100000))
elapsed=time.perf_counter()-start
print("11.",elapsed,"seconds")
