import os
from pydoc_data.topics import topics 
import pandas as pd 
import numpy as np
from tabulate import tabulate

def read_and_load_annotation(filename):
    with open("./Data/ann/" +filename+".ann", "r", encoding="utf-8") as f:
        lines = f.readlines()

    annotation = dict()
    annotation["topics"]=[]
    
    sujets = dict()
    resultat = {"topics" : [],  "negative_keywords" : [], "positive_keywords" : []}

    for l in lines:
        mots = l.split()
        if ("T") in mots[0] and mots[1] == "Subjectiveme_negative":
            resultat["negative_keywords"].append(' '.join(mots[4:]))
        elif ("T") in mots[0] and mots[1] == "Subjectiveme_positive":
            resultat["positive_keywords"].append(' '.join(mots[4:]))
        sujets[mots[0]]= ' '.join(mots[4:])

    for l in lines:
        mots = l.split()
        if "R" in mots[0]:
            if "isPositiveOpinionOn" in mots[1]:
                resultat["topics"].append({"name" : sujets[mots[-1].split(":")[-1]], "opinion": "positive"})
            elif "isNegativeOpinionOn" in mots[1]:
                resultat["topics"].append({"name" : sujets[mots[-1].split(":")[-1]], "opinion": "negative"})
            elif "Negates" in mots[1]:
                resultat["negative_keywords"].append("pas "+sujets[mots[-1].split(":")[-1]])
    return resultat

def load_tweet_with_annotation_first(id):
    if os.path.exists("./Data/tweet/"+id+".txt") and os.stat('./Data/ann/'+id+'.ann').st_size != 0:
        info = {"id":id, "annotation" : read_and_load_annotation(id)}
        with open("./Data/tweet/" +id+".txt", "r", encoding="utf-8") as f:
            info["text"] = f.read()
    else :
        info = None
    return info

def load_tweet_with_annotation(id):
    if os.path.exists("./Data/tweet/"+id+".txt"):
        info = dict()
        info["id"] = id
        if os.stat('./Data/ann/'+id+'.ann').st_size != 0:
            info["annotation"] = read_and_load_annotation(id)
        else: 
            info["annotation"] = None
        with open("./Data/tweet/" +id+".txt", "r", encoding="utf-8") as f:
            info["text"] = f.read()
        return info
    else:
        return None 
        
def load_corpus_in_dataframe(filename):
    with open(filename, "r") as f:
        ids = f.read().splitlines()
    df = pd.DataFrame(columns=['id','text','topics','positive_keywords','negative_keywords'])
    for id in ids: 
        res = load_tweet_with_annotation(id)
        if res != None :
            if  res["annotation"] != None : 
                temp = {"id" : res["id"], "text" : res["text"], "topics": res["annotation"]["topics"], "positive_keywords" : res["annotation"]["positive_keywords"],"negative_keywords" : res["annotation"]["negative_keywords"]}
                df = df.append(temp, ignore_index=True)
            else : 
                temp = {"id" : id, "text" : res["text"], "topics": None , "positive_keywords" : None,"negative_keywords" : None}
                df = df.append(temp, ignore_index=True)
    return df

    
# with open("ids.txt", "w") as f:
#     for i, row in df.iterrows():
#         f.write(row["id"]+'\n')