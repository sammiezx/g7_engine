from fuzzywuzzy import fuzz
import pandas as pd
import numpy as np

# SAMPLE
# enum_set = ['Farmer', 'Doctor']
# word_list = ['frmer', 'faarmer', 'frmr', 'farm', 'farmland', 'dothor', 'dactor', 'engineer']

def fuzz_check(word, enum_set, threshold=50, return_keyword='other'):
    
    # print(word)
    ratio = [(fuzz.ratio(x, word), x) for x in enum_set]
    # print(ratio)
    word = max(ratio)
    if word[0] > threshold:
        return word[1]
    else: 
        return return_keyword




enum_set = ['Inter', '+2', 'NEB', 'BBA', 'BBS', 'Isc', 'BA', 'BSc', 'Civil', 'SEE', 'Undergraduate']
data = {'column1': ['apple', 'banana', 'ssssssssssssss', 'orange', 'other', 'grape', 'kiwi', 'melon']}