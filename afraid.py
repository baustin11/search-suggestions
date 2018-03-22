
# coding: utf-8

# In[8]:


import requests, json
URLafraid="http://suggestqueries.google.com/complete/search?client=firefox&q=i am afraid"
headers = {'User-agent':'Mozilla/5.0'}
responseafraid = requests.get(URLafraid, headers=headers)
afraid = json.loads(responseafraid.content.decode('utf-8'))
print(', '.join(afraid[1][0:1]))
print(', '.join(afraid[1][1:2]))
print(', '.join(afraid[1][2:3]))
print(', '.join(afraid[1][3:4]))

