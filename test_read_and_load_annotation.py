from corpusutils import read_and_load_annotation
from datavisualization.corpusutils import load_tweet_with_annotation
from datavisualization.corpusutils import load_corpus_in_dataframe

from pytest import *
import pandas as pd 

def test_read_and_load_annotation():
    # Given
    filename = "143048389142134785"
    # When
    annotations = read_and_load_annotation(filename)
    #Then
    assert annotations == {'topics' : [{ 'name' : "élection de #missfrance", 'opinion':'negative' }], 'negative_keywords': ['pas plaisir'], 'positive_keywords':['plaisir']}
    # Given
    filename1 = "143059118180139008"
    # When
    annotations1 = read_and_load_annotation(filename1)
    #Then
    assert annotations1 == {'topics' : [{ 'name' : "Languedoc", 'opinion':'positive' },{ 'name' : "Nord-Pas-De-Calais", 'opinion':'negative' } ], 'negative_keywords': ["pas aime"], 'positive_keywords':["jolie", "aime"]}

def test_load_tweet_with_annotation():
    filename = "143048389142134785"
    info = load_tweet_with_annotation(filename)
    assert info == {'id': '143048389142134785', 'annotation': {'topics' : [{ 'name' : "élection de #missfrance", 'opinion':'negative' }], 'negative_keywords': ['pas plaisir'], 'positive_keywords':['plaisir']}, 'text': "Ce soir c'est l'élection de #missfrance et je vais me faire un plaisir de NE PAS regarder."} 
    filename1 = "143059118180139008"
    info = load_tweet_with_annotation(filename1)
    assert info == {'id': '143059118180139008', 'annotation': {'topics' : [{ 'name' : "Languedoc", 'opinion':'positive' },{ 'name' : "Nord-Pas-De-Calais", 'opinion':'negative' } ], 'negative_keywords': ["pas aime"], 'positive_keywords':["jolie", "aime"]}, 'text': "Celle du Languedoc est plutôt jolie. mais j'aime pas vraiment celle du Nord-Pas-De-Calais.. #missfrance"}
    filename2 = "143048457261809664"
    info = load_tweet_with_annotation(filename2)
    assert info == {'id': '143048457261809664', 'annotation': None, 'text': "Ce soir c'est Miss France, pour ceux qui ne le savent pas :D !! #MissFrance"}

def test_load_corpus_in_dataframe():
    filename = 'tweets-ids1'
    donnees = load_corpus_in_dataframe(filename)
    assert donnees.iloc[0]["id"] == '143048389142134785'
    assert donnees.iloc[0]["text"] == "Ce soir c'est l'élection de #missfrance et je vais me faire un plaisir de NE PAS regarder."
    assert donnees.iloc[0]["topics"] == [{'name': 'élection de #missfrance', 'opinion': 'negative'}]
    assert donnees.iloc[1]["id"] == '143048457261809664'
    assert donnees.iloc[1]["text"] == "Ce soir c'est Miss France, pour ceux qui ne le savent pas :D !! #MissFrance"
    assert donnees.iloc[1]["topics"] == None



