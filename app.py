from tensorflow.keras.models import load_model
import streamlit as st
import pandas as pd
from PIL import Image
from utils import *

model = load_model(MODEL_PATH)

st.set_page_config(
  page_title='Vietnamese ABSA', 
  page_icon='https://cdn-icons-png.flaticon.com/512/8090/8090669.png', 
  layout="centered")
st.image(image=Image.open('assets/homepage.png'), caption='Aspect-based Sentiment Analysis')

sentence = st.text_input(label='')

if st.button('Analyze'):
  encoded_sentence = preprocess(sentence)
  pred = model.predict(encoded_sentence)
  pred = pred.reshape(len(ASPECTS), 4)
  pred = np.argmax(pred, axis=-1)
  sentiments = map(lambda x: REPLACEMENTS[x], pred)
  d = []
  for aspect, sentiment in zip(ASPECTS, sentiments): 
    if sentiment: d.append([aspect, sentiment])
  st.markdown('***')
  st.write('**Sentence:**', sentence)
  df = pd.DataFrame(data=d, columns=['Aspect', 'Sentiment'])
  st.table(df)