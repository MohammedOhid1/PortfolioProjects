#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os, shutil


# In[10]:


path = r"C:/Users/ohid1/Documents/Python Tutorials/"


# In[13]:


file_name = os.listdir(path)


# In[18]:


folder_names = ['docx files','image files', 'xlsx files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        #print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
        
for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "xlsx files/" + file):
        shutil.move(path + file, path + "xlsx files/" + file)
    elif ".docx" in file and not os.path.exists(path + "docx files/" + file):
        shutil.move(path + file, path + "docx files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)


# In[17]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




