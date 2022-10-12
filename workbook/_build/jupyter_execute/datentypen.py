#!/usr/bin/env python
# coding: utf-8

# # Datenjournalismus in Python - 
# # Eine praktische Einführung in die Programmierung
# 
# 
# ### Natalie Widmann
# 
# 
# 
# 
# Wintersemester 2022 / 2023
# 
# 
# Universität Leipzig
# 
# 
# 
# 

# # Agenda
# 
# 1. Kurs: Ziele & Organisation
# 2. Motivation - Warum überhaupt programmieren lernen?
# 3. Python als Taschenrechner - Oder wie reich ist Jeff Bezos?
# 4. Von der Praxis zur Theorie
#     - Variablen
#     - Datentypen
#     - Inbuilt Functions
#     - Fehlermeldungen
# 
# 
# 

# # Motivation - Warum überhaupt programmieren lernen?
# 
# 
# 

# ## Daten als Grundlage für Journalismus
# 
# Journalismus basiert fast immer auf Daten. Manchmal sind es nur einzelne Zahlen.
# Aber immer öfter
# Daten helfen uns:
#  
# 
# - Trends zu verstehen
# - Dimensionen greifbar zu machen
# - Ereignisse in Kontext zu setzen
# - in Interaktion mit Leser:innen zu treten

# ![Radmesser](./imgs/radmesser_tagesspiegel.png)

# ![Klimawandel - Morgenpost](./imgs/klimawandel_morgenpost.png)

# ![Merkel nach Zahlen](./imgs/asylantraege_merkel_br.png)

# ## Daten, Daten, Daten
# 
# 
# Manchmal ist die Datenflut so überwältigend, dass Recherchen nur mit technischen Mitteln möglich sind.
# 
# ### Paradise Paper
# 
# - 21 verschiedene Datenquellen
# - ca. 13,4 Millionen Dokumente oder 1,4 Terrabyte an Daten
# - mehr als 380 Journalist:innen aus 67 Ländern
#  
# 

# ![Paradisepaper](./imgs/pardisepaper.png)

# ## Direkte Auswertung & Schnelles Prototyping
# 
# Auch wenn ihr ein Team mit Entwickler:innen, Designer:innen und Co habt, könnt ihr Ideen schnell ausprobieren, Stichprobendaten auswerten und euer Team davon überzeugen.
# 
# 
# ## Digitale Produktentwicklung
# 
# - Aufwände abschätzen
# - Gemeinsame Sprache mit Entwickler:innen
# 
# ## Möglichkeiten kennen und kreativ sein
# 
# - Machinelles Lernen als Hilfsmittel in der Recherche
# - Algortihmischen Bias aufdecken
# - aktueller Stand von Deep Fake Technologie
# 

#     
# ![BR Fake Reviews](./imgs/fakereviews_br.png)
# 
# https://interaktiv.br.de/falsche-google-bewertungen/
# 
# 
# 
# 
# 

# ![Spy Planes](./imgs/spyplanes_buzzfeed.png)
# 
# https://www.buzzfeednews.com/article/peteraldhous/hidden-spy-planes
# 
# 
# 
# 

# ![Machine Bias](./imgs/machinebias_propublica.png)
# 
# https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing
# 
# 
# 
# 
# 
# 

# ![Dalle](./imgs/dalle.png)
# 
# https://openai.com/dall-e-2/
# 
# 
# 
# 
# 

# # Python
# 
# Python wurde 1991 von Guido van Rossom veröffentlicht und ist mittlerweile eine der beliebtesten Programmiersprachen. Gründe dafür sind:
# 
# - die **Vielseitigkeit** - von Datenanalyse und Visualisierung über Webentwicklung bis hin zu maschinellem Lernen
# 
# - die **Einfachheit** - Python ist übersichtlich und leicht zu lernen.
# 
# - **Open Source Community** - die aktive Community behebt Fehler, entwickelt Python stets weiter und hilft bei Problemen
# 

# ![RedMonk Programmiersprachen Ranking](./imgs/redmonk.png)
# 
# 
# 
# 
# 
# 

# # Unser erster Code

# In[1]:


print('Hello World!')



# # Python als Taschenrechner
# 
# Python kann als einfacher Taschenrechner verwendet werden.
# 
# 
# Die Syntax:
# 
# - Die Operatoren +, -, * und / werden wie gewohnt verwendet
# - Mit ** wird potenziert
# - Mit Klammern werden Ausdrücke gruppiert
# - Mit \# beginnt ein Kommentar.
#   Kommentare dienen beschreiben de Code und werden nicht ausgeführt
# 
#         

# In[2]:


# Addition
5 + 6


# In[3]:


# Subtraktion
20 - 4


# In[4]:


# Multiplikation
2 * 6


# In[5]:


# Division
9 / 2


# In[6]:


# Potenzieren
2 ** 3


# In[7]:


# Mit Klammern
(4 + (2 * 3)) * 2


# ![Vergleich zum Reichtum von Jeff Bezos](./imgs/bezos.png)
# 

# # Wie reich ist Jeff Bezos?
# 
# 
# Mit 150 Mrd. USD ist Jeff Bezos auf Platz 4 der reichsten Menschen der Welt.
# 
# 
# ### Beispiele
# 
# Grafik links: Datenvisualisierung von Mona Chalabi in [9 Ways to Imagine Jeff Bezos’ Wealth](https://www.nytimes.com/interactive/2022/04/07/magazine/jeff-bezos-net-worth.html) der New York Times, April 2022.
# 
# 1 Pixel Wealth:
# https://mkorostoff.github.io/1-pixel-wealth/

# # Hands On - Jeff Bezos Wealth
# 
# ## Wie lange muss man arbeiten um so reich zu werden?
# 
# - Mit einem deutschen Durchschnittseinkommen? 
# 
#     Das aktuelle monatliche Durchschnittseinkommen beträgt 4100 Euro brutto bei einer Vollzeitstelle. Für eine Person in Steuerklasse I läuft das auf ca. 1588 Euro netto hinaus.
# 
# 

# In[8]:


# 1. Schritt: USD in € umrechnen (Kurs: 1,03)
print(150000000000 * 1.03)


# In[9]:


# 1. Schritt: USD in € umrechnen (Kurs: 1,03)
vermoegen_in_usd = 150000000000
kurs = 1.03
vermoegen = vermoegen_in_usd * kurs

print(vermoegen)


# In[10]:


# 2. Schritt: Von Monatsgehalt auf durchschnittliches Jahreseinkommen
netto_pro_monat = 1588
einkommen = 12 * netto_pro_monat
print(einkommen)


# In[11]:


# 3. Schritt: Berechnung der Arbeitszeit in Jahren
jahre = vermoegen/ einkommen
print(jahre)


# # Die Welt vor 8 Millionen Jahren...

# <div align="center">
# <img src="./imgs/menschenaffen.png" width="600"/ >
#     
# Vor 8 Millionen Jahren gab es noch keine Menschen auf der Erde. Das Suptropische Klima in Europa kühlt langsam ab und damit sterben auch die meisten europäischen Arten der Menschenartigen aus. Einzig der Oreopithecus überlebt vorest auf einer Insel bei Sardinien/Korsika
# 
# 
# Quelle: http://www.oteripedia.de/Neogen
# </div>
# 
# 

# <div align="center">
# <img src="./imgs/argentavis.png" width="600"/>
#     
# In Südamerika existiert der größte Vogel, der jemals auf der Erde lebte. Der Argentavis magnificens ist wahrscheinlich mit dem Geier verwandt und hat eine Flügelspannweite von 7,20 Metern. Er ist doppelt so groß wie der größte heutige Vogel, der Andenkondor mit 3,30 Metern Flügelspannweite. Die Flügelfläche des Argentavis magnificens beträgt 7 Quadratmeter. Der Vogel wiegt 70-78 Kilogramm. 
# </div>
# 
# 

# ### Wie lange dauert es als Top Manager

# In[12]:


# Wie lange dauert es als Top-Manager so viel Geld anzuhäufen?
einkommen = 100000
jahre = vermoegen/ einkommen
print(jahre)


# ### Die Welt vor 1,5 Millionen Jahren

# ![Homo Erectus](./imgs/homo_erectus.png)
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

# # Zurück zu Jeff Bezos: Was macht man mit so viel Geld?

# In[13]:


vermoegen = 154500000000

# Wie oft könnte er das Banksy's geschreddertes Bild mit Wert von ca. 18,89 Millionen Euro kaufen?
kosten_banksy = 18890000 
anzahl = vermoegen / kosten_banksy
print(anzahl)


# In[14]:


# Wie viele Boeing 737-700 zum Preis von 76 Millionen kann er kaufen?
kosten_boeing737 = 76000000      
anzahl = vermoegen / kosten_boeing737
print(anzahl)


# ## Eine kleines Programm dafür...

# In[15]:


# Wie oft kann Jeff sich X kaufen
vermoegen = 154500000000

dinge = input('Dinge: ')
kosten = input('Kosten:')

anzahl = vermoegen / float(kosten)

antwort = f'Bezos kann sich {anzahl} {ding} zum Preis von {kosten} € kaufen.'
print(antwort)


# # Von der Praxis zur Theorie....

# ## Variablen
# 
# Eine Variable ist die Zuweisung eines Wertes zu einem Namen.
# 
# ```
# <name> = <wert>
# ```
# 

# In[ ]:


pi = 3.141592
print(pi)


# Variablen können sich ändern:

# In[ ]:


favourite_fruit = "banana"
print(favourite_fruit)
favourite_fruit = "strawberry"
print(favourite_fruit)


# In[ ]:


vermoegen = 1200
kosten_fahrrad = 300
vermoegen = vermoegen - kosten_fahrrad
print(vermoegen)


# ## Variablenamen - Regeln & praktische Tipps
# 
# 1. Variablennamen sollten verständlich und aussagekräftig sein
# 
# 2. Variablennamen beginnen immer mit einem Buchstaben oder Unterstrich
# 
# 3. Der Rest des Variablennamens besteht aus Buchstaben, Zahlen oder Unterstrichen
# 
# 4. Variablennamen sind casesensitive (Groß- und Kleinschreibung wird unterschieden)
# 
# 5. Variablennamen können eingebaute Funktionen überscheiben. Daher immer einzigartige, eigenständige Namen verwenden
# 
# 

# 1. Variablennamen sollten verständlich und aussagekräftig sein

# In[ ]:


X = 40075.017
print(X)


# In[ ]:


erdumfang = 40075.017
print(erdumfang)


# 2. Variablennamen beginnen immer mit einem Buchstaben oder Unterstrich

# In[ ]:


€ = 172
print(€)


# In[ ]:


euro = 172
print(euro)


# In[ ]:


10 = 'zehn'


# In[ ]:


_10 = 'zehn'


# 3. Der Rest des Variablennamens kann aus Buchstaben, Zahlen oder Unterstrichen zusammengesetzt sein

# In[ ]:


student_883245_geburtstag = "03.09.1996"


# In[ ]:


student_$10_geburtstag = "21.02.2001"


# 4. Variablennamen sind casesensitive (Groß- und Kleinschreibung wird unterschieden)

# In[ ]:


name = "Gundula"
print(Name)


# 5. Variablennamen können eingebaute Funktionen überscheiben. Daher immer einzigartige, eigenständige Namen verwenden

# In[ ]:


x = 3
y = 7
x = x + y 
z = x - 7
print(z)


# In[ ]:


help(print)
print = "ACHTUNG - Variabelname entspricht dem Namen einer eingebauten Funktion"
print(print)
help(print)


# ## Datentypen
# 
# 
# - **int** - Integer (ganze Zahl) bspw. 4, -72, 12947
# - **float** - Float (Gleitkommazahl) bspw. 3.2, 4.9813, -2.3, 4.0
# - **string** - String bspw. 'Hello', "vorname nachname!"
# - **bool**- Boolean: True oder False
# 
# 
# 

# In[ ]:


a = 2
b = 300
c = -12
d = 90348752
type(a)


# In[ ]:


a + b
type(d / a)


# ## Eingebaute Funktionen
# 
# - sind fester Bestandteil der Programmiersprache
# 
# 
# - Die folgenden Funktionen haben wir schon kennengelernt:
# 
#     - **print** - zeigt den Wert einer Variable in der Konsole
#     - **input** - nimmt Input von Nutzer:innen entgegen 
#     - **type** - gibt den Datentyp einer Variabel oder eines Objektes zurück
#     - **help** - Beschreibung einer Funktion
# 
# 

# In[16]:


help(print)


# In[17]:


help(3)


# ## Fehlermeldungen
# 
# Direktes Feedback dass meist recht genau sagt wo der Fehler liegt:
# 
# 
# 

# In[ ]:


print "zwanzig"


# In[ ]:


'zehn' + 3


# In[ ]:


1_variable = 'wert'


# # Praxis Tipps
# 
# 
# ### #1 Üben, Üben, Üben
# 
# ### #2 Fehler helfen beim Lernen
# 
# ### #3 Lest die Fehlermeldungen
# 
# ### #4 Tauscht euch aus
# 
# 

# In[19]:


def hide_code_in_slideshow():   
    from IPython import display
    import binascii
    import os
    uid = binascii.hexlify(os.urandom(8)).decode()    
    html = """<div id="%s"></div>
    <script type="text/javascript">
        $(function(){
            var p = $("#%s");
            if (p.length==0) return;
            while (!p.hasClass("cell")) {
                p=p.parent();
                if (p.prop("tagName") =="body") return;
            }
            var cell = p;
            cell.find(".input").addClass("hide-in-slideshow")
        });
    </script>""" % (uid, uid)
    display.display_html(html, raw=True)
    
hide_code_in_slideshow()

