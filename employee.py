#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee :
    """(annual) salary"""
    def __init__(self, firstname, lastname, salary) :
        """Initialize private attributes"""
        self.__firstname = firstname
        self.__lastname = lastname
        self.__salary = salary
        
    def give_raise(self, rate=0.02) :
        self.__salary += rate*self.__salary
        return self.__salary

