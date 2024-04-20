#!/usr/bin/env python
# coding: utf-8

# In[4]:


import h5py

# Path to your H5 file
file_path = 'C:/Users/muham/OneDrive/Desktop/Cloud_Attack/cloud_attack_data.h5'

# Open the file in read-only mode
with h5py.File(file_path, 'r') as file:
    # List all groups
    print("Keys: %s" % list(file.keys()))
    if 'performance_metrics' in file:
        data = file['performance_metrics'][()]
        print(data)


# In[ ]:




