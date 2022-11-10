from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import nltk
import os 
import pandas as pd 

# wiki = TextBlob("Miss France : Laury, Malika, Chloé... les brunes super stars jusqu'à Delphine !:   Le 3 décembre, la chaîne TF1 ... http://t.co/r1RFykSr")
# test = TextBlob("Ce soir c'est l'élection de #missfrance et je vais me faire un plaisir de NE PAS regarder.")

# testimonial = wiki.sentiment
# print(testimonial)
# tags = wiki.tags
# print(tags)
# noun  = wiki.noun_phrases
# print(noun)

regions = ['tahiti','provence','champagne','corse','guadeloupe', 'normandie','centre','lorraine','bretagne','reunion','languedoc','picardie','calais','poitou', 'azur', 'pierre','franche','midi','guyan','loire','bourgogne', 'limousin','ile de','martinique','mayotte','orleanais','alsace','aquitaine','loire','caledonie','roussillon','rhone','savoie']
miss = {'tahiti': "Miss Tahiti", 'pierre' : "Miss Saint-Pierre-et-Miquelon", 'roussillon': "Miss Roussillon", 'rhone': "Miss Rhône-Alpes", 'reunion': "Miss Réunion", 'provence': "Miss Provence", 'poitou': "Miss Poitou-Charentes", 'picardie': "Miss Picardie", 'savoie': "Miss Pays de Savoie ",'loire': "Miss Pays de Loire", 'orleanais': "Miss Orléanais", 'caledonie': "Miss Nouvelle Calédonie", 'normandie' : "Miss Normandie", 'calais': "Miss Nord Pas de Calais",'midi': "Miss Midi Pyrénées", "mayotte": "Miss Mayotte", 'martinique': "Miss Martinique", 'lorraine': "Miss Lorraine", 'limousin' : "Miss Limousin", 'languedoc': "Miss Languedoc", 'ile de' : "Miss Ile de France", 'guyan': "Miss Guyane", 'guadeloupe': "Miss Guadeloupe", 'franche': "Miss Franche Comté",'azur': "Miss Cote d'Azur", 'corse': "Miss Corse", 'champagne': "Miss Champagne Ardenne",'centre': "Miss Centre", 'bretagne': "Miss Bretagne", 'bourgogne': "Miss Bourgogne", 'auvergne': "Miss Auvergne", "aquitaine": "Miss Aquitaine", 'alsace': "Miss Alsace"}

def load_tweet_with_textblob(filename):
    info = pd.DataFrame(columns=['id', 'text','opinion','polarite','subjectivite','Nom'])
    with open(filename, "r") as f:
        ids = f.read().splitlines()
    for id in ids: 
        if os.path.exists("./Data/tweet/"+id+".txt"):
            with open("./Data/tweet/" +id+".txt", "r", encoding="utf-8") as f:
                temp = dict()
                temp['id'] = id
                temp["text"] = f.read()
                phrase = TextBlob(temp["text"], pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
                sent = phrase.sentiment
                temp['polarite'] = sent[0]
                temp['subjectivite'] = sent[1]
                trouve = False
                for name in regions:
                    for nom in phrase.noun_phrases:
                        if name in nom:
                            temp["Nom"] = miss[name]
                            if sent[0]<0:
                                temp['opinion'] = 'negative'
                            elif sent[0] == 0:
                                temp['opinion'] = 'neutre'
                            else: 
                                temp['opinion'] = 'positive'                                
                            info = info.append(temp, ignore_index=True)
                            trouve = True
                if not trouve:
                    info = info.append(temp, ignore_index=True)
    return info

df = load_tweet_with_textblob('tweets-ids')
print(df.info())
nb_positive = len(df[df["opinion"]=='positive'])
nb_negative = len(df[df["opinion"]=='negative'])
neutre = len(df[df["opinion"]=='neutre'])
print(nb_positive,nb_negative,neutre)
print(df.dropna())