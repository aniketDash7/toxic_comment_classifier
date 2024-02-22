
import streamlit as st
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import load
model = tf.keras.models.load_model('toxic_comment_classifier.h5')
max_features = 200000
df = pd.read_csv('jigsaw-toxic-comment-classification-challenge/train.csv/train.csv')
vectorizer = TextVectorization(max_tokens=max_features,
                              output_sequence_length=1800,
                              output_mode='int')
vectorizer.adapt(df['comment_text'].values)
def score_comment(comment):
    vectorized_comment = vectorizer([comment])
    vectorized_comment = tf.expand_dims(vectorized_comment, -1)
    results = model.predict(vectorized_comment)
    text = ''
    for idx,col in enumerate(df.columns[2:]):
        text += '{}:{}\n'.format(col,results[0][idx]>0.5)
    return text
    
    return text
def main():
    st.title("Cross your tongue")
    
    comment = st.text_area("Enter your comment:", placeholder="Type your comment here...")
    
    if st.button("Score Comment"):
        results_text = score_comment(comment)
        st.text(results_text)

if __name__ == "__main__":
    main()