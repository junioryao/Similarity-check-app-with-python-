from nltk import sent_tokenize , word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import WordNetLemmatizer,PorterStemmer 
from collections import Counter 
import math 
import numpy as np
import spacy 
import  Custom_analysis 

spacy_nlp = spacy.load('en_core_web_sm')

#special charactere 
speChar  =  set(punctuation)

#stop word 
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
StopWords = set(stopwords.words('english'))

para_1 = '''Messaging platforms are exploding, they now have more users than the social networks. Cynical view - that's a lot of eyeballs that Facebook et al haven't found a way to monetise yet.
 Facebook Messenger's own bot platform is still rapidly evolving. This presents great opportunities but it's a rapidly changing (and therefore potentially expensive and risky) foundation to build on.
 That hasn't stopped some fascinating early movers, including Woebot created by Stanford University to deliver Cognitive Behavioural Therapy, or the UK bot created by a teenager that helped thousands challenge parking tickets and another to help refugees claim asylum.
 In the workplace there are already well-established, paid for Slack bots, including some that we use at Deeson, such as the delightfully named HeyTaco! Slack's latest investment round takes their total to $790m and they have their own bot VC fund.
 Through our research and events and in developing our prototypes for our chatbot build and strategy services we found use cases with clear commercial opportunity that we're developing now. And some use cases that will be firmly staying in the R&D category for a while longer.
 Procter & Gamble pulled $100m of of digital ads as an experiment and sales were... completely unaffected.
 And some reflections from me on why, despite criticism of big brand saturation, I believe the London Pride march has an important job to do in the workplace.
 We'll send you occasional updates when we have something interesting to share. If you'd rather we didn't, you can unsubscribe.
"any interesting fact is emailed."
 '''

para_2 = '''Facebook Messenger's own bot platform is still rapidly evolving. 2)Woebot created by Stanford University to deliver Cognitive Behavioural Therapy, or the UK bot created by a teenager that helped thousands challenge parking tickets and another to help refugees claim asylum. 3)including some that we use at Deeson, such as the delightfully named HeyTaco! 4)Our Technical Strategy Director, Ronald Ashri has been helping clients do just that.

'''



#remove  stop word ,  and sent tokennize the paragraphe 

def sentence_tokennize_stop_word (paragraph):
    collector = []
    for i in sent_tokenize(paragraph) : 
        for j in word_tokenize(i) :
            if j not in StopWords and  j not in speChar and j not in ['0','1','2','3','4','5','6','7','8','9'] and j not in spacy_stopwords and len(j)>2:
                collector.append(j.lower())
    return collector    
      
def word_lemmetizer_stem(words) :
    a = []     
    b = [] 
    for i in words :
        a.append( word1.lemmatize(i) )
        
    for i in a :
        b.append(word2.stem(i))
    return b


# implementation of tf-idf technique 
# 1 ----> 'get TF =  term frequency '
def get_term_frequency (list_element):
    collector = []
    for i in Counter(list_element).items():
        a = i[0]
        b = i[1]
        b =  b / len(Counter(list_element))
        collector.append([a,b])
    return collector 

# 2 ---->  Document inverse frequency 
def idf_evaluator(list_element1 , list_element2):
    idf = []
    for i in list_element1:
        if i in list_element2 :        
            idf.append( [i ,math.log(2/2) ] )
        else: 
            idf.append( [i ,math.log(2/1) ] )
    return idf 
def get_document_inverse_frequency(list_element1 , list_element2):
    idf1 = idf_evaluator(list_element1 , list_element2)
    idf2 = idf_evaluator(list_element2 , list_element1)
    return idf1,idf2 


# perform TF*IDF for each document 
def tf_time_Idf (matrice_of_frequency , idf):
    result = []
    for i in range( len(matrice_of_frequency )):
        result.append(matrice_of_frequency[i][1] * idf[i][1] )
    return result 
        
# apply cos similarities 
def cosin_similarity(element1 , element2):
    ele1 = np.array(element1).reshape(-1,1)
    ele2 = np.array(element2).reshape(-1,1)
    return  (ele1*ele2)/( np.linalg.norm(ele1) * np.linalg.norm(ele2)   )
 
#stemming amd lemmatizer the words object  
word1 = WordNetLemmatizer()
word2 = PorterStemmer() 

para1 = sentence_tokennize_stop_word(para_1)   
para2 = sentence_tokennize_stop_word(para_2) 

para1 = word_lemmetizer_stem(para1)
para2 = word_lemmetizer_stem(para2)

print( word_lemmetizer_stem(para1))
print("/////////////////////////////////////////////////////////////////////")
print( word_lemmetizer_stem(para2))

matrice_of_frequency_1 =  get_term_frequency(para1)
matrice_of_frequency_2 =  get_term_frequency(para2)
idf1 , idf2 = get_document_inverse_frequency((para1),(para2))
# result1 = tf_time_Idf(matrice_of_frequency_1,idf1)
# result2 = tf_time_Idf(matrice_of_frequency_2,idf2)
# simi = cosin_similarity(result1, result2)

print(" ".join(para1))
print(" ".join(para2))
print(Custom_analysis.analysis(" ".join(para1)," ".join(para2)))
