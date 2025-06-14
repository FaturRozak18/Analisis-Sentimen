import pickle
import numpy as np
import streamlit as st

#load save model
model =pickle.load(open('random_forest_final_model.sav.gz','rb'))

#judul web
st.title('Prediction Sentiment Analysis')

stemming_data = st.text_input('Kalimat')

#code for prediction
sentiment_analysis =''

# membuat tombol prediksi
if st.button('Prediction Sentiment'):
    sentiment_prediction = model.predict([[stemming_data]])

    if sentiment_score > 0:
        sentiment_analysis = 'Sentimen Positif'
    elif sentiment_score < 0:
        sentiment_analysis = 'Sentimen Negatif'
    else:
        sentiment_analysis = 'Sentimen Netral'
st.succes(sentiment_analysis)