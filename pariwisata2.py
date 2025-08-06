import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Load the pre-trained model and vectorizer
with open('knn_model.pkl', 'rb') as file:
    knn_model = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Tampilan aplikasi menggunakan Streamlit
st.image("sunan-drajat.jpg")
st.title("Analisis Sentimen Terhadap Objek Wisata Sunan Drajat di Lamongan Menggunakan Metode Algoritma K-Nearest Neighbors (KNN)")

# Input text for sentiment analysis
input_text = st.text_input("Masukkan teks:")
if st.button("Analisis"):
    if input_text:
        # Vectorize the input text
        input_vector = vectorizer.transform([input_text])

        # Perform sentiment analysis using the pre-trained KNN model
        prediction = knn_model.predict(input_vector)

        # Display the sentiment prediction
        st.write("Sentiment:", prediction)
    else:
        st.write("Masukkan teks terlebih dahulu.")

