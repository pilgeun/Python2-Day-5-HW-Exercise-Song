#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def city_info (city, country, population=2880000) :
    """Returns formatted string of City, Country, Population
    
    >>> city_info('Anchorage', 'United States', 288000)
    'Anchorage, United States - population 288,000'
    """
    return f"{city}, {country} - population {population:,}"

print(city_info('Anchorage', 'United States', 288000)) # optional parameter filled in

