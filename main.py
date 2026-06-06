import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Embedding,SimpleRNN,Dense
import streamlit as st
import re
#load all word index
word_index=imdb.get_word_index()
reverse_word_index={value:key for key,value in word_index.items()}
model=load_model('simpleRNN.h5')
## function to decode review
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i-3,'?') for i in encoded_review])
## function to process user input
def preprocess_text(text):
    text=re.sub('[^a-zA-Z]',' ',text)
    words=text.lower().split()
    encoded_review=[word_index.get(word,2)+3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review
## prediction function
def predict_sentiment(review):
    preprocessed_review=preprocess_text(review)
    prediction=model.predict(preprocessed_review)
    sentiment='Positive' if prediction[0][0]>0.5 else 'Negative'
    return sentiment,prediction[0][0]

##streamlit
st.title('IMDB Movie Review Sentiment Analysis')
s='enter a movie review to classify it as possitive or negative.'
st.write(s.capitalize())
User_input=st.text_area('Movie Review')
if st.button('Classify'):
     sentiment,prediction=predict_sentiment(User_input)
     st.write(f"Sentiment: {sentiment}")
     st.write(f"Prediction: {prediction:.2f}")
else:
    st.write('Please Enter movie review')
