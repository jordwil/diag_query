from app import app
from app.prefix_tree import Trie
import pickle
import fnmatch
import os
import json


def get_pickle(pickle_path):
    ''' Looks for pickled data (trie or hash data).  '''
    try:
        return pickle.load(open(pickle_path, 'rb'))
    except:
        return False

def gen_trie(filepath):
    ''' Generates a trie from a newline delim file '''
    my_trie = Trie()
    f = open(filepath, 'r')
    for line in f:
        my_trie.add(line.rstrip())
    f.close
    return my_trie

def update_hash(diag, pre, my_dict):
    '''Ensures the connection between diagnosis and suffix searched
    Holds in a key : list of value format. Creates val list if it's not yet created'''
    try:
        my_dict[diag].append(pre)
    except KeyError:
        my_dict[diag] = [pre]
    return my_dict

def pickle_obj(data, pickle_path):
    ''' Converts data structure into a pickle for storage, overwiting old data '''
    pickle.dump(data, open(pickle_path, 'wb'))

def get_last_ten(my_dict, my_diag):
    ''' Returns the last 10 in a stack format '''
    return my_dict[my_diag][:-11:-1]



trie_filepath = os.path.abspath(os.path.join('app','data', 'my_trie.p'))
diag_pre_filepath = os.path.abspath(os.path.join('app', 'data', 'my_diag_pref.p'))
data_file = os.path.abspath(os.path.join('app', 'data', 'short-diagnoses.txt'))


@app.route('/')
def root_display():
    return 'Hello! Please type in your query into the address bar. http://127.0.0.1:5000/search_term'

@app.route('/<prefix>', defaults={'diag': None}) # Endpoint 1
@app.route('/<prefix>/<diag>') # Endpoint 2
def prefix_display(prefix, diag):
    my_trie = get_pickle(trie_filepath)

    if not my_trie:
        my_trie = gen_trie(data_file)
        pickle_obj(my_trie, trie_filepath) # saves tree

    results = my_trie.start_with_prefix(prefix)

    if not diag: # Endpoint 1
        return 'Results: %s' % results

    my_hash = get_pickle(diag_pre_filepath)

    if not my_hash:
        my_hash = {}

    if diag in tuple(results): # Endpoint 2
        update_hash(diag, prefix, my_hash)
        pickle_obj(my_hash, diag_pre_filepath) # saves hash
        return ('''Your selection %s : %s has been recorded.
         %s selected %s times.
         The last ten prefix entries are: %s''' % (diag, prefix, diag, len(my_hash[diag]), my_hash[diag][:-11:-1]))
