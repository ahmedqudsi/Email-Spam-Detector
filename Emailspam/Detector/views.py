from django.shortcuts import render
import pickle
import os
from .forms import EmailForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model ONCE
with open(os.path.join(BASE_DIR, "model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

def predictemail(email):
    email_vector = vectorizer.transform([email])
    prediction = model.predict(email_vector)
    return "⛔ spam Detected " if prediction[0] == 1 else "✅ This Email Looks Safe"

def home(request):
    result = None
    form = EmailForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["message_content"]
        result = predictemail(email)

    return render(request, "home.html", {
        "form": form,
        "result": result
    })
