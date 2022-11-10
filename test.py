import os 
import codecs

def read_and_load_annotation(filename):
    ids = []
    with open("tweets-ids", "r") as f:
        ids = f.read().splitlines()
        # lines = f.readlines()
        # for line in lines:
        #     ids.append(line)
    dictionnaire  = dict()
    for id in ids: 
        with open("./Data/ann/"+id+".ann", "r", encoding="utf-8") as f:
            lines = f.readlines()
            print(id)
            for line in lines:
                mots = line.split()
                print(mots)
                if len(mots)>1 and mots[1] not in dictionnaire:
                    dictionnaire[mots[1]]=id 
    print(dictionnaire)

def getAllAnnotations(filenname):
    ids = []
    with open("tweets-ids", "r") as f:
        ids = f.read().splitlines()
        lines = f.readlines()
        for line in lines:
            ids.append(line)
    
    anno = [] 
    
    for id in ids:
        with open("./Data/ann/"+id+".ann", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                mots = line.split()
                if mots[1] not in anno:
                    anno.append(mots[1])
    print(anno)

regions = []
misses = {'tahiti': "Miss Tahiti", 'pierre' : "Miss Saint-Pierre-et-Miquelon", 'roussillon': "Miss Roussillon", 'rhone': "Miss Rhône-Alpes", 'reunion': "Miss Réunion", 'provence': "Miss Provence", 'poitou': "Miss Poitou-Charentes", 'picardie': "Miss Picardie", 'savoie': "Miss Pays de Savoie ",'loire': "Miss Pays de Loire", 'orleanais': "Miss Orléanais", 'caledonie': "Miss Nouvelle Calédonie", 'normandie' : "Miss Normandie", 'calais': "Miss Nord Pas de Calais",'midi': "Miss Midi Pyrénées", "mayotte": "Miss Mayotte", 'martinique': "Miss Martinique", 'lorraine': "Miss Lorraine", 'limousin' : "Miss Limousin", 'languedoc': "Miss Languedoc", 'ile de' : "Miss Ile de France", 'guyan': "Miss Guyane", 'guadeloupe': "Miss Guadeloupe", 'franche': "Miss Franche Comté",'azur': "Miss Cote d'Azur", 'corse': "Miss Corse", 'champagne': "Miss Champagne Ardenne",'centre': "Miss Centre", 'bretagne': "Miss Bretagne", 'bourgogne': "Miss Bourgogne", 'auvergne': "Miss Auvergne", "aquitaine": "Miss Aquitaine", 'alsace': "Miss Alsace"}
# for key, miss in misses:
    # regions.append(miss)
print(misses.values())

# read_and_load_annotation("Bonjour")
getAllAnnotations("tweets-ids")