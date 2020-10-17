import dandelion
from dandelion import DataTXT
token = 'e60ec5fe0ca848b8bf218c97f9f72b84'
from dandelion import default_config
default_config['token'] = token
datatxt = DataTXT()


    
def analysis(t1,t2):
    semantic=datatxt.sim(t1,t2,binow = 'never')    
    return  round( semantic['similarity']*100  , 2 )