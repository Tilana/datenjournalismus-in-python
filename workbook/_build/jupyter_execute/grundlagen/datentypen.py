#!/usr/bin/env python
# coding: utf-8

# # Datentypen 
# 
# Jede Information in Python hat einen Datentyp. 
# Je nach Datentyp sind bestimmte Berechnungen oder Methoden verfügbar.
# 
# Die grundlegenden Datentypen:
# 
# 
# | Datentyp  | Beschreibung  | Beispiel |
# |----------|:-------------  |:-------- |
# | int |  *integer* - ganze Zahl |  3, 9031, 0, -18|
# | float |  Kommazahl | 2.4, -99.99, 0.007 |
# | string | Zeichenkette | "Hello", '23.9', 'String mit Zahlen 123' |
# | bool |  *boolean* - Wahrheitswerte | True, False |
# 

# ## Abfrage Datentyp
# 
# Der Datentyp einer Variable kann mit `type()` abgefragt werden.

# In[1]:


type(-3200191)


# In[2]:


type(23.8)


# In[3]:


type('Hello World')


# In[4]:


type(True)


# ## Ändern des Datentyps - Type Castings
# 
# Der Datentyp einer Variable kann mithilfe der gleichnamigen Funktionen abgeändert werden. Dies wird auch *Type Casting* genannt.

# In[5]:


# Von float zu...
value = 5.7
print(value)
print(type(value))

# von float zu int
var = int(value)
print(var)
print(type(var))

# von float zu string
var = str(value)
print(var)
print(type(var))

# von float zu bool
var = bool(value)
print(var)
print(type(var))


# In[6]:


# Von int... 
value = 5
print(value)
print(type(value))

# von int zu float
var = float(value)
print(var)
print(type(var))

# von int zu string
var = str(value)
print(var)
print(type(var))

# von int zu boolean
var = bool(value)
print(var)
print(type(var))


# In[7]:


# Von string zu ... 
value = '3.2'
print(value)
print(type(value))

# von string zu float
var = float(value)
print(var)
print(type(var))

# von string zu boolean
var = bool(value)
print(var)
print(type(var))


# In[8]:


# Von boolean zu...
value = False
print(value)
print(type(value))

# von bool zu int
var = int(value)
print(var)
print(type(var))

# von bool zu float
var = float(value)
print(var)
print(type(var))

# von bool zu string
var = str(value)
print(var)
print(type(var))


# :::warning
# 
# Die Umwandlung zwischen Datentypen, beispielsweise von *string* zu *int*, funktioniert nur wenn der string den Datentyp, in unserem Beispiel eine ganze Zahl und eben nur diese, beinhaltet.
# 
# :::

# In[9]:


# String mit ganzer Zahl zu int
value = '-982'
var = int(value)
print(var)
print(type(var))


# In[10]:


# von string zu int
value = '5.6'
var = int(value)
print(var)
print(type(var))


# In[17]:


# von string zu int
value = 'Eine ganze Zahl 6 mit anderen Zeichen'
var = int(value)
print(var)
print(type(var))


# In[ ]:




