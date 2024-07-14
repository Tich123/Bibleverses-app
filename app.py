from flask import Flask,render_template,request,url_for
import pandas as pd 
import numpy as np 

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

# NLP
from textblob import TextBlob 

app = Flask(__name__)
