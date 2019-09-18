#!/usr/bin/env python
# coding: utf-8

# In[14]:


lst1 = ['A','a']
lst2 = tuple(lst1)


# In[15]:


lst2


# In[3]:


lst5=[]


# In[4]:


for i in range(26):
    lst1=[chr(ord('A')+i),chr(ord('a')+i)]
    lst2=tuple(lst1)
    lst5.append(lst2)


# In[5]:


lst5


# In[6]:


for j in range(26):
    print(lst5[j][0],'-',lst5[j][1])


# In[ ]:




