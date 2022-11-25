WORD2ID_PKL = 'output/word2id.pkl'
MODEL_PATH  = 'output/absa_bi-lstm.h5'

ASPECTS = ['BATTERY', 'CAMERA', 'DESIGN', 'FEATURES', 'GENERAL', 'PERFORMANCE', 'PRICE', 'SCREEN', 'SER&ACC', 'STORAGE']
REPLACEMENTS = {0: None, 1: 'Positive', 2: 'Negative', 3: 'Neutral'}

SEQUENCE_LENGTH = 75