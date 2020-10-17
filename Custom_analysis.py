
import dandelion
from dandelion import DataTXT
token = '3d86a1a88bc4456c91f82a0d6043a31f'

from dandelion import default_config
default_config['token'] = token
datatxt = DataTXT()


def analysis(t1 ,t2 ):

#"never" uses always the semantic algorithm
    semantic=datatxt.sim(t1,t2,binow = 'never')
    return  round( semantic['similarity']*100  , 2 )
