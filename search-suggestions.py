
# coding: utf-8

# In[1]:


import requests, json
URL="http://suggestqueries.google.com/complete/search?client=firefox&q=hello world"
headers = {'User-agent':'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
result = json.loads(response.content.decode('utf-8'))
print(result)


