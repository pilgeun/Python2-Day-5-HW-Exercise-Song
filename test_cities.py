#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from city_functions import city_info

class CityTestCase(unittest.TestCase) :
    """Test for 'city_functions.py'"""
    
    def test_city_country(self) :
        """Testing city = 'Anchorage', country = 'United States'"""
    
        result = city_info('Anchorage','United States') # 
        self.assertEqual(result, 'Anchorage, United States - population 288,000')
        
    def test_city_country_population(self) :
        """Testing city = 'Anchorage', country = 'United States, population = 288000"""
        result = city_info('Anchorage','United States', 288000)
        self.assertEqual(result, 'Anchorage, United States - population 288,000')
 
unittest.main()

