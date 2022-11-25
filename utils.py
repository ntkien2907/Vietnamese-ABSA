from tensorflow.keras.preprocessing import sequence as sq
import numpy as np
import pickle
from config import *

with open(WORD2ID_PKL, 'rb') as f:
    word2id = pickle.load(f)

def indexing(sentence):
    words = sentence.split()
    ids = [word2id[word] if word in word2id.keys() else 0 for word in words]
    return np.array(ids)

def preprocess(sentence):
    comment = indexing(sentence)
    comment = sq.pad_sequences([comment], maxlen=SEQUENCE_LENGTH)
    return comment