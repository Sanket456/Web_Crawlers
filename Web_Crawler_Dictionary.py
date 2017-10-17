
# coding: utf-8

# In[4]:

import re
import urllib.request
try:
    url = "http://dictionary.reference.com/browse/"
    data = input("Enter the Word you wand to search for")
    url = url + data
    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")
    m = re.search('meta name="description" content="',data1)
    start = m.end()
    end = start + 300
    newString = data1[start:end]
    m = re.search('See more.',newString)
    end = m.start() - 1
    newString1 = newString[0:end]
    print(newString1)
except:
    print('Sorry!Word Cannot be found out')


# In[ ]:




# In[ ]:




# In[ ]:



