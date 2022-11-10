import pandas as pd 
from sympy import false, true
import unidecode
import matplotlib.pyplot as plt

from corpusutils import load_corpus_in_dataframe
from corpus_statistics import getTopics


# df = load_corpus_in_dataframe("tweets-ids")
# df_test = df[:150]
# print(df[df['id']== '143072165888139264'])
# topics = getTopics(df_test)[0]
# topics = getTopics(df)[0]
# print(topics[topics['id']== '143072165888139264'])



# regions = ['tahiti','provence','champagne','corse','guadeloupe', 'normandie','centre','lorraine','bretagne','reunion','languedoc','picardie','calais','poitou', 'azur', 'pierre','franche','midi','guyan','loire','bourgogne', 'limousin','ile de','martinique','mayotte','orleanais','alsace','aquitaine','loire','caledonie','roussillon','rhone','savoie']
# miss = {'tahiti': "Miss Tahiti", 'pierre' : "Miss Saint-Pierre-et-Miquelon", 'roussillon': "Miss Roussillon", 'rhone': "Miss Rhône-Alpes", 'reunion': "Miss Réunion", 'provence': "Miss Provence", 'poitou': "Miss Poitou-Charentes", 'picardie': "Miss Picardie", 'savoie': "Miss Pays de Savoie ",'loire': "Miss Pays de Loire", 'orleanais': "Miss Orléanais", 'caledonie': "Miss Nouvelle Calédonie", 'normandie' : "Miss Normandie", 'calais': "Miss Nord Pas de Calais",'midi': "Miss Midi Pyrénées", "mayotte": "Miss Mayotte", 'martinique': "Miss Martinique", 'lorraine': "Miss Lorraine", 'limousin' : "Miss Limousin", 'languedoc': "Miss Languedoc", 'ile de' : "Miss Ile de France", 'guyan': "Miss Guyane", 'guadeloupe': "Miss Guadeloupe", 'franche': "Miss Franche Comté",'azur': "Miss Cote d'Azur", 'corse': "Miss Corse", 'champagne': "Miss Champagne Ardenne",'centre': "Miss Centre", 'bretagne': "Miss Bretagne", 'bourgogne': "Miss Bourgogne", 'auvergne': "Miss Auvergne", "aquitaine": "Miss Aquitaine", 'alsace': "Miss Alsace"}
# missNames = {'delphine': 'Miss Alsace', 'wespiser':'Miss Alsace', 'mathilde': 'Miss Pays de Loire', 'couly':'Miss Pays de Loire', 'marie': 'Miss Réunion', 'payet':'Miss Réunion', 'solene': 'Miss Provence', 'froment':'Miss Provence','charlotte':"Miss Cote d'Azur", 'murray':"Miss Cote d'Azur"}

# print(topics.info())

def getAllNames(df):
    liste = []
    for index, row in df.iterrows():
        if row["topics"]:
            for elt in row["topics"]: 
                name = unidecode.unidecode(elt["name"].lower())
                if ("miss" in name or "Miss" in name) and name not in liste:
                    if not "france" in name:
                        liste.append(name)
    return liste

def annotate(topics, regions, miss, missNames):
    temp = []
    for index, row in topics.iterrows():
        flag = None
        # if 'miss' in row["topic"]:
        for name in regions: 
            if name in row["topic"]:
                flag = miss[name]
                break
        temp.append(flag)
        for name in missNames.keys() : 
            if name in row["topic"]:
                flag = missNames[name]
                break
    annotations = topics.assign(Nom = temp)
    return annotations

def annotateTextblob(topics, regions, miss, missNames):
    temp = []
    for index, row in topics.iterrows():
        flag = None
        # if 'miss' in row["topic"]:
        for name in regions: 
            if name in unidecode.unidecode(row["text"].lower()):
                flag = miss[name]
                break
        temp.append(flag)
        for name in missNames.keys() : 
            if name in row["text"]:
                flag = missNames[name]
                break
    annotations = topics.assign(Nom = temp)
    return annotations

def printStatAllMisses(annotations, regions, miss):
    stat = pd.DataFrame(columns=['Nom','nb_positif','nb_negatif'])
    for name in regions: 
        temp = {'Nom' : miss[name]}
        temp['nb_positif'] = len(annotations[(annotations['Nom']== miss[name]) & (annotations['opinion']=='positive') ])
        temp['nb_negatif'] = len(annotations[(annotations['Nom']== miss[name]) & (annotations['opinion']=='negative') ])
        stat = stat.append(temp, ignore_index=True)
    print(stat)
    return stat


def plotStat(stat, title):
    label = stat['Nom'].to_list()
    pos = stat["nb_positif"].to_list()
    neg = stat["nb_negatif"].to_list()
    stat = stat.sort_values(by=["nb_positif"], ascending=False)
    stat.plot(y= ["nb_positif","nb_negatif"], x='Nom', kind='bar', color={"nb_positif": "#008000", "nb_negatif": "red"}, )
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plotAllStat(stat, stat_blob):
    stat = stat.sort_values(by=["Nom"])
    stat_blob = stat_blob.sort_values(by=["Nom"])
    stat_blob = stat_blob.rename(columns={"Nom": "Nom_TextBlob", "nb_positif": "nb_positif_textBlob", "nb_negatif": "nb_negatif_textBlob"})
    result = pd.concat([stat, stat_blob], axis=1, join='outer')
    result = result.sort_values(by=["nb_positif"], ascending=False)
    result.plot(y= ["nb_positif","nb_negatif","nb_positif_textBlob","nb_negatif_textBlob"], x='Nom', kind='bar', color={"nb_positif": "#008000", "nb_negatif": "#B22222","nb_positif_textBlob":"#00FA9A", "nb_negatif_textBlob":"#DC143C" }, )
    plt.tight_layout()
    plt.title("Répartition des avis par Miss selon les annotations et Textblob")
    plt.show()
    print(result)
    print(result.info())
    
    


# annotations = annotate(topics, regions, miss, missNames) 
# print(annotations.info())

# print(annotations[annotations["Nom"]=='Miss Aquitaine'])
# print(annotations[annotations['id']== '143072165888139264'])

# annotations = printStatAllMisses(annotations)
# plotStat(annotations)

# print(annotations.info())

        



