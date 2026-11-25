#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## Introduction
# 
# This project is about analyzing employee data using Python.
# 
# ### Objectives
# - Understand employee data.
# - Perform data analysis.
# - Compare Python execution time.

# 

# In[1]:


print("Welcome to Employee Data Analysis")


# In[ ]:





# ## Python List Comprehension vs For Loop

# In[2]:


numbers = list(range(100000))

get_ipython().run_line_magic('timeit', '[x * 2 for x in numbers]')


# In[4]:


numbers = list(range(100000))

def for_loop():
    result = []
    for x in numbers:
        result.append(x * 2)
    return result

get_ipython().run_line_magic('timeit', 'for_loop()')


# In[5]:


get_ipython().run_line_magic('timeit', '[x * 2 for x in numbers]')


# In[ ]:





# ## Conclusion
# 
# List comprehension is a simple and shorter way to create a list.
# 
# A for loop is useful when we need multiple statements
# or complex operations.
# 
# Both methods can be used depending on the requirement.

# 
