from gensim.models.keyedvectors import KeyedVectors
model_path = 'GoogleNews-vectors-negative300.bin'
w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=True)
from DocSim import DocSim
ds = DocSim(w2v_model)


def getscore(right , wrong) :

    source_doc = right
    target_docs = [wrong]
    
    # This will return 3 target docs with similarity score
    
    sim_scores = ds.calculate_similarity(source_doc, target_docs)
    return round( sim_scores[0]['score']*100 , 2 )
    
    

