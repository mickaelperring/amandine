import streamlit as st
import random
import pandas as pd
import string
import unicodedata
from Global import G
from gpt import chatGPT

G.init('lettresProposees', [])
G.init("mot", '')
G.init('lettresfausses', [])
G.init('tirets', '')
#######################################
listedemots = ['CUISINE','CLASSEUR','TIRELIRE','SUISSE','GRASSOUILLET','POIDS','SABLE','BILLARD','BRIQUET','CARNAVAL','MONOCHROME','VISITEUR','CERF','FLAMENCO','INJECTER','CASSEROLE','JUPITER','CLIMATISATION','BEURRE',"ABRICOT", "ANTILOPE", "ASTRONAUTE", "AUTOMOBILE", "AVION", "BALCON", "BIBLIOTHEQUE", "BLAGUE", "BOISSON",
    "BOUTEILLE", "CAHIER", "CAMION", "CANARD", "CAPITALE", "CARTE", "CHAISE", "CHAMBRE", "CHIEN", "CHOCOLAT", 
    "CITROUILLE", "CLAVIER", "CLE", "COIN", "COLLINE", "COQUILLAGE", "CORBEILLE", "CRAYON", "CUISINE", "DENTIFRICE",
    "DICTIONNAIRE", "DINOSAURE", "ECRAN", "ECRIVAIN", "ELEPHANT", "EMISSION", "ENERGIE", "ESCARGOT", "ETOILE",
    "FERME", "FEUILLE", "FLEUR", "FONTAINE", "FORET", "FRIGO", "GANT", "GARE", "GATEAU", "GIRAFFE", "HORLOGE", 
    "HOTEL", "ILE", "IMMEUBLE", "INSECTE", "INTERNET", "JARDIN", "JOURNAL", "JUPE", "LAC"]


if G.mot == '' :
    initiale_au_hasard = random.choice(string.ascii_uppercase)
    lettre_au_hasard = random.choice(string.ascii_uppercase)
    G.mot = chatGPT.question(f'donne moi un nom commun pas composé qui commence par {initiale_au_hasard} et qui contient {lettre_au_hasard}')
    G.mot = G.mot.upper()
    G.mot = G.mot.replace('.', '')
    def remove_accents(input_str):
        sansaccents = unicodedata.normalize('NFD', input_str)
        only_ascii = ''.join([c for c in sansaccents if not unicodedata.combining(c)])
        return only_ascii
    G.mot = remove_accents(G.mot)
    

    #G.mot = random.choice(listedemots) 
#st.write(G.mot)

st.title(f'trouve le mot' )

#proposition = st.text_input('taper votre lettre')
#proposition = proposition.upper()


proposition = ''
cols = st.columns(10)
contenu_colonnes = ['A','Z','E','R','T','Y','U','I','O','P','Q','S','D','F','G','H','J','K','L','M','W','X','C','V','B','N']
if len(G.lettresfausses) == 13 or G.tirets == G.mot:
    pass
else:
    for i in range(len(contenu_colonnes)):
        lettre_bouton = contenu_colonnes[i]
        if cols[i % 10].button(lettre_bouton, disabled = lettre_bouton in G.lettresProposees):
            proposition = lettre_bouton
G.lettresProposees.append(proposition)



G.tirets = ''
for lettre in G.mot:
    if lettre in G.lettresProposees:
        G.tirets = G.tirets + lettre
    else:
        G.tirets = G.tirets + '-'
st.title(G.tirets)





if G.tirets == G.mot:
  st.image('grenouille.png', width = 200)
  st.balloons()

if not proposition in G.mot:
    if not proposition in G.lettresfausses:
        G.lettresfausses.append(proposition)



st.write('-'.join(G.lettresfausses))

if len(G.lettresfausses)> 1:
    st.write(f'vous avez fait {len(G.lettresfausses)} fautes')
else:
    st.write(f'vous avez fait {len(G.lettresfausses)} faute')

st.image(f'pendu-{len(G.lettresfausses)}.png', width = 300)

if len(G.lettresfausses) == 13:
  st.write(f'Raté, le mot était {G.mot} ')

    

