#!/usr/bin/env python
# coding: utf-8
Write a function to compute 5/0 and use try/except to catch the exceptions.
# In[13]:


try :
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except :
    print ("The answer is infinity please entered correct number")
else :
    print("exceuted sucessfully")

Implement a Python program to generate all sentences where subject is in ["Americans",
"Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
# In[3]:


subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]


# In[8]:


final_result = [(sub + " "+ vb + " "+ ob + " ")for sub in subjects for vb in verbs for ob in objects]
for i in final_result:
    print(i)


# Write a function so that the columns of the output matrix are powers of the input vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when
# increasing is False, the i-th output column is the input vector raised element-wise to the power
# of N - i - 1.

# In[13]:


import numpy as np
a=np.array([1,2,3,4])
np.vander(a)


# In[17]:


np.column_stack([a**(N-i-1) for i in range(N)])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




