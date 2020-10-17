import analysisPackage
from nltk.corpus import stopwords
from string import punctuation
from collections import Counter 
import spacy 
import gensim 
from nltk import word_tokenize,WordNetLemmatizer
spacy_nlp = spacy.load('en_core_web_sm')

#special charactere 
speChar  =  set(punctuation)

#stop word 
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
StopWords = set(stopwords.words('english'))

para_1 = '''Ronald Ashir (Deeson) can help define a bot strategy
Deeson benchmarks the industry
Deeson builds high value digital solutions

 '''

para_2 = '''
The second paragraph and the three first bullet points are defining the context and explain what a chat bot is: - "Bots is an unhelpfully broad label that covers everything from the latest Natural Language Processing AI research to our old friend Eliza" - "Messaging platforms are exploding ..." - "Facebook Messenger's own bot platform is still rapidly evolving." - "That hasn't stopped some fascinating early movers ..." Then the two last bullet points are Deeson current position regarding this technology: - "In the workplace there are already well-established, paid for Slack bots ..." - "Through our research and events and in developing our prototype ... "  The last bullet point is interesting as it close the general overview of the technology by explaining Deeson current R&D and commercial solutions. Finally the conclusion, "In conclusion, don't blindly jump on the bandwagon but do make sure you've got a strategy that allows you to keep pace.", is there to strengthen Deeson position as a premium interlocutor for this matter. Indeed, it is Deeson opinion that this matter is not as easy as it seems and that clients need a strategy and help to develop this technology. Help that Deeson provides

'''
#lemmetization process 

def lemmetization(text_list):
    collector = [] 
    for i in word_tokenize(text_list):
        #first lemma process 
        collector.append( WordNetLemmatizer().lemmatize(i))
    return collector 

  
#remove  stop word 

def remove_stop_word (paragraph):
    collector = []
    for j in (paragraph) : 
            if j not in StopWords and  j not in speChar and j not in ['0','1','2','3','4','5','6','7','8','9'] and j not in spacy_stopwords and len(j)>3:
                collector.append(j.lower())
    return collector    

def remove_duplicate_element(text):
    return [i for i in  Counter(text).keys()]

# p = lemmetization(para_1)
# x = remove_stop_word(p)


# p1 =lemmetization(para_2)
# x1 = remove_stop_word(p1)
# x1 = remove_duplicate_element(x1)


#create a unique ID for each word using gensim corpora 
def get_corpora_unique_ID(ele1_goal , ele2_check ):
    return gensim.corpora.Dictionary([ele1_goal,ele2_check])


#unique_id = get_corpora_unique_ID(x,x1)
#unique_id.token2id to display all element from the geensim dict



 


def Do_all(para_1 ,para_2 ):
   
    p = lemmetization(para_1)
    x = remove_stop_word(p)
    p1 =lemmetization(para_2)
    x1 = remove_stop_word(p1)
    x1 = remove_duplicate_element(x1)
    return analysisPackage.analysis(" ".join(x)," ".join(x1))    























