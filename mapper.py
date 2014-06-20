# Starting point for this code is the example given here: 
# http://h3manth.com/content/word-frequency-mapreduce-python
# (Thanks Hemanth.HM for making it available)

#!/python

#!/usr/bin/python2.6                                                                                                                                                                                      
#                                                                                                                                                                                                         
# Copyright [2011] Hemanth.HM                                                                                                                                                                             
#                                                                                                                                                                                                         
# Licensed under the Apache License, Version 2.0 (the "License");                                                                                                                                         
# you may not use this file except in compliance with the License.                                                                                                                                        
# You may obtain a copy of the License at                                                                                                                                                                 
#                                                                                                                                                                                                         
#   http://www.apache.org/licenses/LICENSE-2.0                                                                                                                                                            
#                                                                                                                                                                                                         
# Unless required by applicable law or agreed to in writing, software                                                                                                                                     
# distributed under the License is distributed on an "AS IS" BASIS,                                                                                                                                       
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                                                                                                                
# See the License for the specific language governing permissions and                                                                                                                                     
# limitations under the License.                                                                                                                                                                          

import collections
import string
import re
import operator
import sys
import json

__authors__ = "Hemanth HM <hemanth.hm@gmail.com>"
__version__ = "1.0"

class MapReduce:
    """ Linear implementation of MapReduce.                                                                                                                                                               
    MapReduce is a software framework introduced by Google.                                                                                                                                               
    """

    def map_it(self,lines):
        """ Returns a list of lists of the form [word,1]                                                                                                                                                  
            for each element in the list that was passed.                                                                                                                                                 
        """
        return [[word, 1] for word in lines]

    def sort_it(self,wlist):
        """ Returns a list of list of the form [word,[partialcounts]] """
        res = collections.defaultdict(list)
        map(lambda w: res[w[0]].append(w[1]), wlist)
        return res.items()

    def map_reduce(self,wlist):
        """ Returns a dict with word : count mapping """
        results = {}
        for res in self.sort_it(self.map_it(wlist)) :
            results[res[0]] = sum(res[1])
        return results


class SlurpFile:
    """ Simple class to get the file contents, after filtering punctuations                                                                                                                               
                                                                                                                                                                                                          
    Attributes:                                                                                                                                                                                           
        fpath: Path to the file name.                                                                                                                                                                     
    """

    stoplist = (['for','to','the','a','that','do','on','be',
                 'is','in','of','as','can','are','this','from',
                 'thats','they','if','see','some','but','not','yes',
                 'we','We','when','then','which','though','take',
                 'an','It','Is','them','and','it','will','have','you',
                 'there','about','you','or','was','has','had',
                 'more','so','at','would','should','could','The',
                 'how','their','here','out','with','ok','one','want',
                 'what','also','right','into','your','us','no','its',
                 'week','dont','I','my','i','me','am','too','did','just',
                 'any','good','like','get'
                ])

    def __init__(self,path):
        """ Inits the SlurpFile class with path to the file                                                                                                                                               
        Args:                                                                                                                                                                                             
            path: path to the file that needs to be read.                                                                                                                                                 
        """
        self.fpath = path

    def get_contents(self):
        """ Read the files and cleans it by removing the punctuations                                                                                                                                     
            and returns a list of words.                                                                                                                                                                  
        """
        #with open(self.fpath) as wfile:
        with open('/dev/input', 'r') as wfile:
            all_words = ''.join(ch for ch in wfile.read() if ch not in set(string.punctuation)).split()

            filtered_words = []
            for word in all_words:
                if word not in self.stoplist and not word.isdigit() and not word.startswith('http'):
                    filtered_words.append(word)

            return filtered_words

       
mr = MapReduce()

slurp = SlurpFile('/dev/input')
result = mr.map_reduce(slurp.get_contents())

sorted_result = sorted(result.iteritems(), key=operator.itemgetter(1), reverse=True)


with open('/dev/out/reducer', 'a') as f:
	f.write(json.dumps(sorted_result))

