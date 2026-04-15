import streamlit as st
from transformers import pipeline
est.cache_resource
def load summarizer():
  return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
