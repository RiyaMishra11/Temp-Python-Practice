# 111 Unit Testing Practice
import unittest

# 1 Add
def add(a,b): return a+b
class TestAdd(unittest.TestCase):
    def test_add(self): self.assertEqual(add(2,3),5)

# 2 Subtract
def subtract(a,b): return a-b
class TestSubtract(unittest.TestCase):
    def test_subtract(self): self.assertEqual(subtract(10,4),6)

# 3 Reverse
def reverse_text(x): return x[::-1]
class TestReverse(unittest.TestCase):
    def test_reverse(self): self.assertEqual(reverse_text("Python"),"nohtyP")

# 4 Boolean assertions
def is_even(n): return n%2==0
class TestEven(unittest.TestCase):
    def test_even(self): self.assertTrue(is_even(10))
    def test_odd(self): self.assertFalse(is_even(7))

# 5 Comparison assertions
class TestComparison(unittest.TestCase):
    def test_values(self):
        self.assertGreater(10,5)
        self.assertLess(3,8)

# 6 List assertion
def numbers(): return [1,2,3,4]
class TestList(unittest.TestCase):
    def test_list(self): self.assertEqual(numbers(),[1,2,3,4])

# 7 Dictionary assertion
def user(name,age): return {"name":name,"age":age}
class TestUser(unittest.TestCase):
    def test_user(self): self.assertDictEqual(user("Aman",22),{"name":"Aman","age":22})

# 8 Exception test
def divide(a,b):
    if b==0: raise ValueError("Cannot divide by zero")
    return a/b
class TestDivide(unittest.TestCase):
    def test_zero(self):
        with self.assertRaises(ValueError): divide(10,0)

# 9 setUp
class Calculator:
    def multiply(self,a,b): return a*b
class TestCalculator(unittest.TestCase):
    def setUp(self): self.c=Calculator()
    def test_multiply(self): self.assertEqual(self.c.multiply(4,5),20)

# 10 subTest
class TestCases(unittest.TestCase):
    def test_cases(self):
        for a,b,e in [(2,3,5),(5,5,10),(-1,1,0)]:
            with self.subTest(a=a,b=b): self.assertEqual(add(a,b),e)

# 11 Run all tests
if __name__=="__main__":
    unittest.main()
