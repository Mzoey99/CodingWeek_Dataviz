from corpusutils import load_corpus_in_dataframe
from corpus_statistics import getTopics
from corpus_statistics import printStatiques
from annotation_analysis import annotate, printStatAllMisses, plotStat, annotateTextblob
from tutoTextBlob import load_tweet_with_textblob



regions = ['tahiti','provence','champagne','corse','guadeloupe', 'normandie','centre','lorraine','bretagne','reunion','languedoc','picardie','calais','poitou', 'azur', 'pierre','franche','midi','guyan','loire','bourgogne', 'limousin','ile de','martinique','mayotte','orleanais','alsace','aquitaine','loire','caledonie','roussillon','rhone','savoie']
miss = {'tahiti': "Miss Tahiti", 'pierre' : "Miss Saint-Pierre-et-Miquelon", 'roussillon': "Miss Roussillon", 'rhone': "Miss Rhône-Alpes", 'reunion': "Miss Réunion", 'provence': "Miss Provence", 'poitou': "Miss Poitou-Charentes", 'picardie': "Miss Picardie", 'savoie': "Miss Pays de Savoie ",'loire': "Miss Pays de Loire", 'orleanais': "Miss Orléanais", 'caledonie': "Miss Nouvelle Calédonie", 'normandie' : "Miss Normandie", 'calais': "Miss Nord Pas de Calais",'midi': "Miss Midi Pyrénées", "mayotte": "Miss Mayotte", 'martinique': "Miss Martinique", 'lorraine': "Miss Lorraine", 'limousin' : "Miss Limousin", 'languedoc': "Miss Languedoc", 'ile de' : "Miss Ile de France", 'guyan': "Miss Guyane", 'guadeloupe': "Miss Guadeloupe", 'franche': "Miss Franche Comté",'azur': "Miss Cote d'Azur", 'corse': "Miss Corse", 'champagne': "Miss Champagne Ardenne",'centre': "Miss Centre", 'bretagne': "Miss Bretagne", 'bourgogne': "Miss Bourgogne", 'auvergne': "Miss Auvergne", "aquitaine": "Miss Aquitaine", 'alsace': "Miss Alsace"}
missNames = {'delphine': 'Miss Alsace', 'wespiser':'Miss Alsace', 'mathilde': 'Miss Pays de Loire', 'couly':'Miss Pays de Loire', 'marie': 'Miss Réunion', 'payet':'Miss Réunion', 'solene': 'Miss Provence', 'froment':'Miss Provence','charlotte':"Miss Cote d'Azur", 'murray':"Miss Cote d'Azur"}

def main(): 
    # print("Bonjour Lapinou")
    # df = load_corpus_in_dataframe("tweets-ids")
    # topics = getTopics(df)[0]
    # # printStatiques(df,topics)
    # nb_tweets = len(df)
    # print( "Nombre de tweets :", nb_tweets )
    # print(df.info())
    # topics, positive_words,negative_words = getTopics(df)
    # nb_positive = len(topics[topics["opinion"]=='positive'])
    # nb_negative = len(topics[topics["opinion"]=='negative'])
    # print(topics.info())
    # print("Nombre d'opinion positive", nb_positive)
    # print("Nombre d'opinion négative", nb_negative)
    # print("nombre de mots positifs", len(positive_words))
    # print("nombre de mots negatifs", len(negative_words))
    # annotations = annotate(topics, regions, miss, missNames)
    info_textblob = load_tweet_with_textblob("tweets-ids")

    annotations = annotateTextblob(info_textblob, regions, miss, missNames)
    print(annotations.dropna())

    nb_positive = len(info_textblob[info_textblob["opinion"]=='positive'])
    nb_negative = len(info_textblob[info_textblob["opinion"]=='negative'])
    neutre = len(info_textblob[info_textblob["opinion"]=='neutre'])
    print(nb_positive,nb_negative,neutre)
    stat = printStatAllMisses(annotations, regions,miss)
    plotStat(stat)


if __name__ == '__main__':
    main()