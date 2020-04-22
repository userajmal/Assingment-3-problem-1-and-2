#!/usr/bin/env python
# coding: utf-8
Write a function to compute 5/0 and use try/except to catch the exceptions.
# In[1]:


try :
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except :
    print ("The entered Number is infinity please entered correct number")
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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




