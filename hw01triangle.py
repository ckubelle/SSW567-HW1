
import unittest 
import math

def classify_triangle(a,b,c):

    if a == b and b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        if int(a*a + b*b) == int(c*c):
            return "Right Isosceles"
        else:
            return "Isosceles"
    
    if int(a*a + b*b) == int(c*c):
        return "Right"

    return "Scalene"


class TestTriangles(unittest.TestCase):

    def testEquilateral(self):
        self.assertEqual(classify_triangle(5,5,5),'Equilateral','5,5,5 is a Equilateral triangle')
        self.assertEqual(classify_triangle(10,10,10),'Equilateral','10,10,10 is a Equilateral triangle')

    def testIsosceles(self):
        self.assertEqual(classify_triangle(7,7,10),'Isosceles','7,7,10 is a Isosceles triangle')
        self.assertEqual(classify_triangle(10,7,10),'Isosceles','10,7,10 is a Isosceles triangle')
        self.assertEqual(classify_triangle(7,10,10),'Isosceles','7,10,10 is a Isosceles triangle')
        self.assertEqual(classify_triangle(15,15,15*math.sqrt(2)),'Right Isosceles','15,15,15sqrt(2) is a Right Isosceles triangle')

    def testRight(self):
        self.assertEqual(classify_triangle(3,4,5), 'Right', '3,4,5 is a Right Triangle')
        self.assertEqual(classify_triangle(6,8,10), 'Right', '6,8,10 is a Right Triangle')
        #This next test case is to show a bug in my program, that if the values are converted to ints, then small changes in lengths will still result in the same answer
        self.assertEqual(classify_triangle(3.1,4,5), 'Right', '3.1,4,5 is a Right Triangle')

    def testScalene(self):
        self.assertEqual(classify_triangle(2,3,5), 'Scalene', '2,3,5 is a Scalene Triangle')
        self.assertEqual(classify_triangle(123,234234,506786), 'Scalene', '123,234234,506786 is a Scalene Triangle')
        self.assertEqual(classify_triangle(33,4123,5123123123), 'Scalene', '33,4123,5123123123 is a Scalene Triangle')
        

if __name__ == '__main__':
    unittest.main(exit=True)
    
    
       
       