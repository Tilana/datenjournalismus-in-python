#!/usr/bin/env python
# coding: utf-8

# # Wie reich ist Jeff Bezos?
# 
# 
# Mit 150 Mrd. USD ist Jeff Bezos auf Platz 4 der reichsten Menschen der Welt.
# 
# 
# ### Datenvisualisierung
# 
# 1 Pixel Wealth:
# https://mkorostoff.github.io/1-pixel-wealth/
# 

# ![Vergleich zum Reichtum von Jeff Bezos](../../imgs/bezos.png)
# 
# 
# Datenvisualisierung von Mona Chalabi in [9 Ways to Imagine Jeff Bezos’ Wealth](https://www.nytimes.com/interactive/2022/04/07/magazine/jeff-bezos-net-worth.html) der New York Times, April 2022.
# 

# ## Wie lange muss man arbeiten um so reich wie Jeff Bezos zu werden?
# 
# Das aktuelle monatliche Durchschnittseinkommen in Deutschland beträgt 4100 Euro brutto bei einer Vollzeitstelle.
# 
# 
# Für eine Person in Steuerklasse I läuft das auf ca. 1588 Euro netto hinaus.
# 
# 

# In[1]:


# 1. Schritt: USD in € umrechnen (Kurs: 1,03)
print(150000000000 * 1.03)


# In[2]:


# 1. Schritt: USD in € umrechnen (Kurs: 1,03)
vermoegen_in_usd = 150000000000
kurs = 1.03
vermoegen = vermoegen_in_usd * kurs

print(vermoegen)


# In[3]:


# 2. Schritt: Von Monatsgehalt auf durchschnittliches Jahreseinkommen
netto_pro_monat = 1588
einkommen = 12 * netto_pro_monat
print(einkommen)


# In[4]:


# 3. Schritt: Berechnung der Arbeitszeit in Jahren
jahre = vermoegen/ einkommen
print(jahre)


# ### Die Welt vor 8 Millionen Jahren...

# ![Menschenaffen](../../imgs/menschenaffen.png)
# 
# Vor 8 Millionen Jahren gab es noch keine Menschen auf der Erde. Das Suptropische Klima in Europa kühlt langsam ab und damit sterben auch die meisten europäischen Arten der Menschenartigen aus. Einzig der Oreopithecus überlebt vorest auf einer Insel bei Sardinien/Korsika
# 

# 
# ![Argentavis](../../imgs/argentavis.png)
#     
# In Südamerika existiert der größte Vogel, der jemals auf der Erde lebte. Der Argentavis magnificens ist wahrscheinlich mit dem Geier verwandt und hat eine Flügelspannweite von 7,20 Metern. Er ist doppelt so groß wie der größte heutige Vogel, der Andenkondor mit 3,30 Metern Flügelspannweite. Die Flügelfläche des Argentavis magnificens beträgt 7 Quadratmeter. Der Vogel wiegt 70-78 Kilogramm.

# ## Wie lange muss man mit einem Spitzengehalt sparen?

# In[5]:


# Wie lange dauert es als Top-Manager so viel Geld anzuhäufen?
einkommen = 100000
jahre = vermoegen/ einkommen
print(jahre)


# ### Die Welt vor 1,5 Millionen Jahren

# ![Homo Erectus](../../imgs/homo_erectus.png)
# 
# 

# Im heutigen Kenia lebt der Homo erectus. Er benutzt Faustkeile und ist wahrscheinlich in der Lage Feuer zu machen.
# 
# Bis er Europa erreicht vergehen weitere 300.000 Jahre.
# 
# 
# 
# 
# 
# 
# 
# Quelle: http://www.oteripedia.de/Pleistoz%C3%A4n

# ## Was kann man mit so viel Geld machen?

# In[6]:


vermoegen = 154500000000

# Wie oft könnte er das Banksy's geschreddertes Bild mit Wert von ca. 18,89 Millionen Euro kaufen?
kosten_banksy = 18890000 
anzahl = vermoegen / kosten_banksy
print(anzahl)


# In[7]:


# Wie viele Boeing 737-700 zum Preis von 76 Millionen kann er kaufen?
kosten_boeing737 = 76000000      
anzahl = vermoegen / kosten_boeing737
print(anzahl)


# ## Eine kleines Programm dafür...

# In[2]:


# Wie oft kann Jeff sich X kaufen
vermoegen = 154500000000

dinge = input('Dinge: ')
kosten = input('Kosten:')

anzahl = vermoegen / float(kosten)

antwort = f'Bezos kann sich {anzahl} {dinge} zum Preis von {kosten} € kaufen.'
print(antwort)


# In[ ]:




