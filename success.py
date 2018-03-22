
# coding: utf-8


# In[55]:


import requests, json
title="success is counted sweetest" 
URLsuccess="http://suggestqueries.google.com/complete/search?client=firefox&q=success"
headers = {'User-agent':'Mozilla/5.0'}
responsesuccess = requests.get(URLsuccess, headers=headers)
resultsuccess = json.loads(responsesuccess.content.decode('utf-8'))

print(', '.join(resultsuccess[1][0:1]))
print(', '.join(resultsuccess[1][1:2]))
print(', '.join(resultsuccess[1][2:3]))
print(title)



