#!/usr/bin/env python
# coding: utf-8

# ## Variablen
# 
# Eine Variable ist die Zuweisung eines Wertes zu einem Namen.
# 
# 
# #### Syntax
# 
# ```
# <name> = <wert>
# ```
# 
# 
# **Beispiel**

# In[1]:


pi = 3.141592
print(pi)


# Variablen können sich ändern:

# In[2]:


# Beispiel 1
favourite_fruit = "banana"
print(favourite_fruit)
favourite_fruit = "strawberry"
print(favourite_fruit)


# In[3]:


# Beispiel 2
vermoegen = 1200
print(vermoegen)
kosten_fahrrad = 300
vermoegen = vermoegen - kosten_fahrrad
print(vermoegen)


# ### Variablenamen - Regeln & praktische Tipps
# 
# 
# Variablennamen...
# 
# - ... sollten verständlich und aussagekräftig sein
# 
# - ... bestehen aus Buchstaben, Zahlen oder Unterstrichen
# 
# - ... beginnen immer mit einem Buchstaben oder Unterstrich
# 
# - ... case-sensitive, das heißt Groß- und Kleinschreibung wird unterschieden
# 
# 

# 
# 
# ::: {warning}
# 
# Variablennamen können eingebaute Funktionen oder Schlüsselwörter überscheiben.
# 
# Daher immer unbesetzte Namen verwenden.
# 
# :::
# 
# 
# 

# **Variablennamen sollten verständlich und aussagekräftig sein**

# In[4]:


X = 40075.017
print(X)


# vs.

# In[5]:


erdumfang = 40075.017
print(erdumfang)


# **Variablennamen bestehen kann aus Buchstaben, Zahlen oder Unterstrichen** 

# In[6]:


student_883245_geburtstag = "03.09.1996"


# In[7]:


student_$10_geburtstag = "21.02.2001"


# **Variablennamen beginnen immer mit einem Buchstaben oder Unterstrich**

# In[ ]:


# Beispiel 1
€ = 172   # €
print(€)


# vs.

# In[ ]:


euro = 172
print(euro)


# In[ ]:


# Beispiel 2
10 = 'zehn'


# vs.

# In[ ]:


_10 = 'zehn'


# **Variablennamen sind case-sensitive**

# In[ ]:


name = "Gundula"
print(Name)


# vs.

# In[ ]:


print(name)


# **Variablennamen können eingebaute Funktionen überscheiben**

# In[ ]:


print('Hello')
print = "ACHTUNG - Variablename entspricht dem Namen einer eingebauten Funktion"
print('Hello')


# Eindeutige und nicht vergebene Variablennamen verhindern diesen Fehler.
# 
# Ist es doch mal passiert, dass eine eingebaute Funktion oder ein Schlüsselwort überschrieben wurde, hilft es, die Variable umzubenennen und Python (in Jupyter Notebooks den Kernel) neu zu starten.

# 
