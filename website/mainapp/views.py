from django.shortcuts import render
from django.contrib import messages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string
import pickle
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
vectorization = TfidfVectorizer()
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def fake(request):
    return render(request, 'frontend/fake.html')
    
def faksubmit(request):
    textarea=request.POST['textarea']
    # with open(', 'rb+') as f:
    listdata=[]
    def wordopt(text):
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub("\\W"," ",text) 
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)    
        return text
    def output_lable(n):
        if n == 0:
            listdata.append('Fake News')
        elif n == 1:
            listdata.append('True News')
    
    def manual_testing(news):
        testing_news = {"text":[news]}
        new_def_test = pd.DataFrame(testing_news)
        new_def_test["text"] = new_def_test["text"].apply(wordopt) 
        new_x_test = new_def_test["text"]
        df = pd.read_csv("templates/pkl/manual_testing2.csv")
        x = df["text"]
        y = df["class"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
        xv_train = vectorization.fit_transform(x_train)
        new_xv_test = vectorization.transform(new_x_test)
        LR.fit(xv_train,y_train)
        pred_LR = LR.predict(new_xv_test)
        return output_lable(pred_LR[0])
        
    news = str(textarea)
    manual_testing(news)
    print(listdata)
    
    context={'textarea' : textarea, 'listdata':listdata}
    messages.success(request, 'Your Result is : True')
    return render(request, 'frontend/fake.html',{'context':context})