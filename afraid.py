
# coding: utf-8

# In[1]:


import requests, json
URL="http://suggestqueries.google.com/complete/search?client=firefox&q=tell"
headers = {'User-agent':'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
result = json.loads(response.content.decode('utf-8'))



# In[22]:


result


# In[ ]:


result[1]


# In[25]:


result[1][:3]


# In[26]:


print(', '.join(result[1]))


# In[30]:


import requests, json
URLtest="http://suggestqueries.google.com/complete/search?client=firefox&q=hello"
headers = {'User-agent':'Mozilla/5.0'}
responsetest = requests.get(URLtest, headers=headers)
resulttest = json.loads(responsetest.content.decode('utf-8'))
print(', '.join(resulttest[1]))


# In[31]:


import requests, json
URLtoday="http://suggestqueries.google.com/complete/search?client=firefox&q=today i"
headers = {'User-agent':'Mozilla/5.0'}
responsetoday = requests.get(URLtoday, headers=headers)
resulttoday = json.loads(responsetoday.content.decode('utf-8'))
print(', '.join(resulttoday[1]))


# In[39]:


print(', '.join(resulttoday[1][:5]))
print(', '.join(resulttest[1][:5]))


# In[40]:


print(', '.join(resulttoday[1][:5]))
print(', '.join(resulttest[1][:5]))
print(', '.join(resulttoday[1][6:10]))


# In[46]:


print(', '.join(resulttoday[1][0:1]))
print(', '.join(resulttest[1][0:1]))
print(', '.join(resulttoday[1][1:2]))
print(', '.join(resulttest[1][1:2]))
print(', '.join(resulttoday[1][2:3]))
print(', '.join(resulttest[1][2:3]))


# In[51]:


print(', '.join(resulttoday[1][0:1]))
print(', '.join(resulttoday[1][1:2]))
print(', '.join(resulttoday[1][2:3]))


# In[52]:


word="abcd"


# In[53]:


print(', '.join(resulttoday[1][0:1]))
print(', '.join(resulttoday[1][1:2]))
print(', '.join(resulttoday[1][2:3]))
print(word)


# In[55]:


import requests, json
title="success is counted sweetest" 
URLsuccess="http://suggestqueries.google.com/complete/search?client=firefox&q=success"
headers = {'User-agent':'Mozilla/5.0'}
responsesuccess = requests.get(URLsuccess, headers=headers)
resultsuccess = json.loads(responsesuccess.content.decode('utf-8'))
print(', '.join(resultsuccess[1]))


# In[56]:


print(', '.join(resultsuccess[1][0:1]))
print(', '.join(resultsuccess[1][1:2]))
print(', '.join(resultsuccess[1][2:3]))
print(title)


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

