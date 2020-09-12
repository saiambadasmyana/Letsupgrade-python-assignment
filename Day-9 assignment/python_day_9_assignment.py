# -*- coding: utf-8 -*-
"""Python day-9 assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19SrPAN-8fQvZnJC0enmz8lb1YAIu-iyr

##Write a python Function for finding is a given number prime or not and do Unit Testing on it using
PyLint and Unittest Library.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile test_primeone.py
# '''
# This is a module to check weather the given number is prime of not.''
# '''
# def prime(number):
#     '''
#     This is the main function which check out the given number is prime or not.
#     '''
#     if number>1:
#         for i in range(2, number):
#             if number % i == 0:
#                 return "not a prime"
#         return "it's a prime"

! pylint "test_primeone.py"

# Commented out IPython magic to ensure Python compatibility.
# %%writefile testing1.py
#  
# import unittest
# import test_primeone
#  
# class Flower(unittest.TestCase):
#     
#     def test_jasmine(self):
#         n=10
#         num=test_primeone.prime(n)
#         self.assertEqual(num,"not a prime")
#         
# if __name__ == "__main__":
#     unittest.main()

! python testing1.py

"""##Make a small generator program for returning armstrong numbers in between 1-1000 in a
generator object.
"""

def Armstrong(lst):
    for number in lst:
        order=len(str(number))
        temp=number
        sum=0
        while temp>0:
            d=temp%10
            sum=sum+d**order
            temp=temp//10
        if number==sum:
            yield number

lst = list(range(1,1001))
print(list(Armstrong(lst)))
