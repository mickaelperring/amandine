import streamlit as st
import random
import pandas as pd
from Global import G
from gpt import chatGPT

G.init('lettresProposees', [])
G.init('nombredefautes',0)
G.init("mot", '')
#######################################
listedemots = ['CUISINE','CLASSEUR','TIRELIRE','SUISSE','GRASSOUILLET','POIDS','SABLE','BILLARD','BRIQUET','CARNAVAL','MONOCHROME','VISITEUR','CERF','FLAMENCO','INJECTER','CASSEROLE','JUPITER','CLIMATISATION','BEURRE',"ABRICOT", "ANTILOPE", "ASTRONAUTE", "AUTOMOBILE", "AVION", "BALCON", "BIBLIOTHEQUE", "BLAGUE", "BOISSON",
    "BOUTEILLE", "CAHIER", "CAMION", "CANARD", "CAPITALE", "CARTE", "CHAISE", "CHAMBRE", "CHIEN", "CHOCOLAT", 
    "CITROUILLE", "CLAVIER", "CLE", "COIN", "COLLINE", "COQUILLAGE", "CORBEILLE", "CRAYON", "CUISINE", "DENTIFRICE",
    "DICTIONNAIRE", "DINOSAURE", "ECRAN", "ECRIVAIN", "ELEPHANT", "EMISSION", "ENERGIE", "ESCARGOT", "ETOILE",
    "FERME", "FEUILLE", "FLEUR", "FONTAINE", "FORET", "FRIGO", "GANT", "GARE", "GATEAU", "GIRAFFE", "HORLOGE", 
    "HOTEL", "ILE", "IMMEUBLE", "INSECTE", "INTERNET", "JARDIN", "JOURNAL", "JUPE", "LAC"]

if G.mot == '' :
    G.mot = chatGPT.question('donne moi un mot aléatoire de la langue française en majuscule')
    G.mot = random.choice(listedemots) 

st.title(f'trouve le mot' )

#proposition = st.text_input('taper votre lettre')
#proposition = proposition.upper()


cols = st.columns(10)
contenu_colonnes = ['A','Z','E','R','T','Y','U','I','O','P','Q','S','D','F','G','H','J','K','L','M','W','X','C','V','B','N']
for i in range(len(contenu_colonnes)):
        if cols[i % 10].button(contenu_colonnes[i]):
            proposition = contenu_colonnes[i]

G.lettresProposees.append(proposition)
st.write(proposition)
tirets = ''
for lettre in G.mot:
    if lettre in G.lettresProposees:
        tirets = tirets + lettre
    else:
        tirets = tirets + '-'
st.title(tirets)

if tirets == G.mot:
  st.image('grenouille.png')
  st.balloons()

if not proposition in G.mot:
    G.nombredefautes = G.nombredefautes + 1
st.write(G.nombredefautes)
st.image(f'pendu-{G.nombredefautes}.png')
if G.nombredefautes == 13:
  st.write(f'Raté, le mot était {G.mot} ')
    

