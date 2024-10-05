from django.shortcuts import render

# Create your views here.
import pandas as pd
from django.shortcuts import render
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from .forms import MessageForm


dataset = pd.read_csv('C:/Users/harsh/OneDrive/Documents/skillbridge/emails.csv')

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(dataset['text'])

X_train, X_test, y_train, y_test = train_test_split(X, dataset['spam'], test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)


def predict_message(message):
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)
    return 'Spam' if prediction[0] == 1 else 'Ham'


def Home(request):
    result = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['text']
            result = predict_message(message)
    else:
        form = MessageForm()
        
    return render(request, 'home.html', {'form': form, 'result': result})
