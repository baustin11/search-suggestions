
# coding: utf-8

# In[5]:


import requests, json
URLa="http://suggestqueries.google.com/complete/search?client=firefox&q=a"
headers = {'User-agent':'Mozilla/5.0'}
responsea = requests.get(URLa, headers=headers)
a = json.loads(responsea.content.decode('utf-8'))

URLb="http://suggestqueries.google.com/complete/search?client=firefox&q=b"
responseb = requests.get(URLb, headers=headers)
b = json.loads(responseb.content.decode('utf-8'))

URLc="http://suggestqueries.google.com/complete/search?client=firefox&q=c"
responsec = requests.get(URLc, headers=headers)
c = json.loads(responsec.content.decode('utf-8'))

URLd="http://suggestqueries.google.com/complete/search?client=firefox&q=d"
responsed = requests.get(URLd, headers=headers)
d = json.loads(responsed.content.decode('utf-8'))

URLe="http://suggestqueries.google.com/complete/search?client=firefox&q=e"
responsee = requests.get(URLe, headers=headers)
e = json.loads(responsee.content.decode('utf-8'))

URLf="http://suggestqueries.google.com/complete/search?client=firefox&q=f"
responsef = requests.get(URLf, headers=headers)
f = json.loads(responsef.content.decode('utf-8'))

URLg="http://suggestqueries.google.com/complete/search?client=firefox&q=g"
responseg = requests.get(URLg, headers=headers)
g = json.loads(responseg.content.decode('utf-8'))

URLh="http://suggestqueries.google.com/complete/search?client=firefox&q=h"
responseh = requests.get(URLh, headers=headers)
h = json.loads(responseh.content.decode('utf-8'))

URLi="http://suggestqueries.google.com/complete/search?client=firefox&q=i"
responsei = requests.get(URLi, headers=headers)
i = json.loads(responsei.content.decode('utf-8'))

URLj="http://suggestqueries.google.com/complete/search?client=firefox&q=j"
responsej = requests.get(URLj, headers=headers)
j = json.loads(responsej.content.decode('utf-8'))

URLk="http://suggestqueries.google.com/complete/search?client=firefox&q=k"
responsek = requests.get(URLk, headers=headers)
k = json.loads(responsek.content.decode('utf-8'))

URLl="http://suggestqueries.google.com/complete/search?client=firefox&q=l"
responsel = requests.get(URLl, headers=headers)
l = json.loads(responsel.content.decode('utf-8'))

URLm="http://suggestqueries.google.com/complete/search?client=firefox&q=m"
responsem = requests.get(URLm, headers=headers)
m = json.loads(responsem.content.decode('utf-8'))

URLn="http://suggestqueries.google.com/complete/search?client=firefox&q=n"
responsen = requests.get(URLn, headers=headers)
n = json.loads(responsen.content.decode('utf-8'))

URLo="http://suggestqueries.google.com/complete/search?client=firefox&q=o"
responseo = requests.get(URLo, headers=headers)
o = json.loads(responseo.content.decode('utf-8'))

URLo="http://suggestqueries.google.com/complete/search?client=firefox&q=o"
responseo = requests.get(URLo, headers=headers)
o = json.loads(responseo.content.decode('utf-8'))

URLp="http://suggestqueries.google.com/complete/search?client=firefox&q=p"
responsep = requests.get(URLp, headers=headers)
p = json.loads(responsep.content.decode('utf-8'))

URLq="http://suggestqueries.google.com/complete/search?client=firefox&q=q"
responseq = requests.get(URLq, headers=headers)
q = json.loads(responseq.content.decode('utf-8'))

URLr="http://suggestqueries.google.com/complete/search?client=firefox&q=r"
responser = requests.get(URLr, headers=headers)
r = json.loads(responser.content.decode('utf-8'))

URLs="http://suggestqueries.google.com/complete/search?client=firefox&q=s"
responses = requests.get(URLs, headers=headers)
s = json.loads(responses.content.decode('utf-8'))

URLt="http://suggestqueries.google.com/complete/search?client=firefox&q=t"
responset = requests.get(URLt, headers=headers)
t = json.loads(responset.content.decode('utf-8'))

URLu="http://suggestqueries.google.com/complete/search?client=firefox&q=u"
responseu = requests.get(URLu, headers=headers)
u = json.loads(responseu.content.decode('utf-8'))

URLv="http://suggestqueries.google.com/complete/search?client=firefox&q=v"
responsev = requests.get(URLv, headers=headers)
v = json.loads(responsev.content.decode('utf-8'))

URLw="http://suggestqueries.google.com/complete/search?client=firefox&q=w"
responsew = requests.get(URLw, headers=headers)
w = json.loads(responsew.content.decode('utf-8'))

URLx="http://suggestqueries.google.com/complete/search?client=firefox&q=x"
responsex = requests.get(URLx, headers=headers)
x = json.loads(responsex.content.decode('utf-8'))

URLy="http://suggestqueries.google.com/complete/search?client=firefox&q=y"
responsey = requests.get(URLy, headers=headers)
y = json.loads(responsey.content.decode('utf-8'))

URLz="http://suggestqueries.google.com/complete/search?client=firefox&q=z"
responsez = requests.get(URLz, headers=headers)
z = json.loads(responsez.content.decode('utf-8'))


print(', '.join(a[1][0:1]))
print(', '.join(b[1][0:1]))
print(', '.join(c[1][0:1]))
print(', '.join(d[1][0:1]))
print(', '.join(e[1][0:1]))
print(', '.join(f[1][0:1]))
print(', '.join(g[1][0:1]))
print(', '.join(h[1][0:1]))
print(', '.join(i[1][0:1]))
print(', '.join(j[1][0:1]))
print(', '.join(k[1][0:1]))
print(', '.join(l[1][0:1]))
print(', '.join(m[1][0:1]))
print(', '.join(n[1][0:1]))
print(', '.join(o[1][0:1]))
print(', '.join(p[1][0:1]))
print(', '.join(q[1][0:1]))
print(', '.join(r[1][0:1]))
print(', '.join(s[1][0:1]))
print(', '.join(t[1][0:1]))
print(', '.join(u[1][0:1]))
print(', '.join(v[1][0:1]))
print(', '.join(w[1][0:1]))
print(', '.join(x[1][0:1]))
print(', '.join(y[1][0:1]))
print(', '.join(z[1][0:1]))

