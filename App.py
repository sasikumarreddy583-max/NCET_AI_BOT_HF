import streamlit as st
from transformers import pipeline
est.cache_resource
def load summarizer():
  return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
summarizer = load summarizer()
st.title(" AI Text Summarizer")
st.write("Enter a long text below, and get a concise summary!")
long_text = st.text_area("Enter text to sumarize:", height=200)
max_length = st.slider("max Sumary Length", nin_value=50, 
                         max_ value=300, value=130)
min_ length = st.slider("min Sumary Length", ain_value=20, 
                          max_value=100, value=30)
if st.button("Summarize"):
    if long_text.strip():
        with st.spinner("Generating summary... "):
            summary = summarizer(long_text, max_length=max_length, min_length=min_length, do_sample=False)
        st.subheader(" Summary:")
        st.success(summary[0]['summary_text'])
    else:
        st.warning(" Please enter some text to summarize.")
