# pylint: disable=C0103
# (ignoring Snake case error, using camelCase)
# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    '''Testing triangles'''
    # define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self):
        '''Testing right triangle'''
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self):
        '''Testing Right triangle'''
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testEquilateralTriangles(self):
        '''Testing equilateral triangle'''
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be Equilateral')
    def testIsoscelesTriangles(self):
        '''Testing isosceles triangle'''
        self.assertEqual(classify_triangle(6,6,8),'Isosceles', "6,6,8 should be Isosceles")
    def testScaleneTriangles(self):
        '''Testing scalene triangle'''
        self.assertEqual(classify_triangle(4,5,6),'Scalene', "4,5,6 should be Scalene")
    def testNotTriangles(self):
        '''Testing not a triangle'''
        self.assertEqual(classify_triangle(10,15,30),'NotATriangle', "10,15,30 NotATriangle")
    def testInputs1(self):
        '''Testing InvalidInput'''
        self.assertEqual(classify_triangle(201,15,30),'InvalidInput', "InvalidInput")
    def testInputs2(self):
        '''Testing InvalidInput'''
        self.assertEqual(classify_triangle(0,15,30),'InvalidInput', "InvalidInput")
    def testInputs3(self):
        '''Testing InvalidInput'''
        self.assertEqual(classify_triangle('a',15,30),'InvalidInput', "InvalidInput")

if __name__ == '__main__':
    print('Running unit tests')
    print (classify_triangle(1,1,1))
    unittest.main()
