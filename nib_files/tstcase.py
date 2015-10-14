import unittest
def fun(x):
    return x+1
def add(a,b):
    return a+b
class A:
    def __init__(self,age):
        self.a=45
    def display(self):
        return self.a

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3),4)
    def testadd(self):
        self.assertEqual(add(3,4),7)
    def testB(self):
        self.assertEqual(A(45).display(),45)
unittest.main()
