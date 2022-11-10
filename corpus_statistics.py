from corpusutils import load_corpus_in_dataframe
import pandas as pd 
import matplotlib.pyplot as plt
import unidecode
import argparse


def getTopics(df):
    topics = pd.DataFrame(columns=['id','topic','opinion'])
    positive_words = []
    negative_words = []
    for index, row in df.iterrows():
        if row["topics"]:
            for elt in row["topics"]: 
                topics = topics.append({"id" : row["id"], "topic" : unidecode.unidecode(elt["name"].lower()), "opinion" : elt ["opinion"]}, ignore_index=True)
        if row["negative_keywords"]:
            negative_words.append(row["negative_keywords"])
        if row["positive_keywords"]:
            positive_words.append(row["positive_keywords"])
    return topics, positive_words, negative_words

def printStatiques(df, topics): 
    nb_tweets = len(df)
    print( "Nombre de tweets :", nb_tweets )
    print(df.info())
    topics, positive_words,negative_words = getTopics(df)
    nb_positive = len(topics[topics["opinion"]=='positive'])
    nb_negative = len(topics[topics["opinion"]=='negative'])
    print(topics.info())
    print("Nombre d'opinion positive", nb_positive)
    print("Nombre d'opinion négative", nb_negative)
    print("nombre de mots positifs", len(positive_words))
    print("nombre de mots negatifs", len(negative_words))
    return 0 
    

