#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from employee import Employee

class test_Employee(unittest.TestCase) :
    """Test for employee.py"""
    def setUp(self) :
        """creating multiple levels of a custom raise to use in test cases"""
        self.employee1 = Employee("Miguel", "Diaz", 100)
        self.raises = [0.04, 0.1, 0.5]
    
    def test_give_default_raise(self) :
        """"""
        result = self.employee1.give_raise()
        self.assertEqual(result, 102.0)

    def test_give_custom_raise(self, rate) :
        salaries = []
        for rate in self.raises :
            salaries.append(give_raise[rate])
            
        self.assertEqual(salaries, [104.0,110.0,150.0])
        

unittest.main()

