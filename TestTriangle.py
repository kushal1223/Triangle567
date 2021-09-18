# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be Equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(6,6,8),'Isosceles', "6,6,8 should be Isosceles")

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(4,5,6),'Scalene', "4,5,6 should be Scalene")

    def testNotTriangles(self):
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle', "10,15,30 should be NotATriangle")

if __name__ == '__main__':
    print('Running unit tests')
    print (classifyTriangle(1,1,1))
    unittest.main()

