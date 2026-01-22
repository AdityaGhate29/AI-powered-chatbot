import os
import json
import random
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

# --------------------------------------------------
# BASE DIRECTORY (PATH SAFE)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------
# NLTK SETUP (Windows)
# --------------------------------------------------
nltk.data.path.append('C:/nltk_data')

lemmatizer = WordNetLemmatizer()

# --------------------------------------------------
# LOAD INTENTS DATA
# --------------------------------------------------
intents_path = os.path.join(BASE_DIR, '..', 'data', 'intents.json')

if not os.path.exists(intents_path):
    raise FileNotFoundError(f"intents.json not found at {intents_path}")

with open(intents_path, 'r', encoding='utf-8') as file:
    intents = json.load(file)

# --------------------------------------------------
# PREPARE VOCABULARY & CLASSES
# --------------------------------------------------
words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        documents.append((tokens, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = sorted(set([
    lemmatizer.lemmatize(word.lower())
    for word in words
    if word not in ignore_letters
]))

classes = sorted(set(classes))

# --------------------------------------------------
# LOAD TRAINED MODEL (AUTO DETECT .keras OR .h5)
# --------------------------------------------------
model_dir = os.path.join(BASE_DIR, '..', 'model')

model_keras = os.path.join(model_dir, 'chatbot_model.keras')
model_h5 = os.path.join(model_dir, 'chatbot_model.h5')

if os.path.exists(model_keras):
    model_path = model_keras
elif os.path.exists(model_h5):
    model_path = model_h5
else:
    raise FileNotFoundError(
        "No model file found. Expected chatbot_model.keras or chatbot_model.h5 inside /model folder"
    )

model = load_model(model_path)

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def clean_up_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in tokens]


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)

    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1

    return np.array(bag)


def predict_intent(sentence):
    bow = bag_of_words(sentence)
    probabilities = model.predict(np.array([bow]), verbose=0)[0]
    return classes[np.argmax(probabilities)]


def get_response(intent_tag):
    for intent in intents['intents']:
        if intent['tag'] == intent_tag:
            return random.choice(intent['responses'])


def chat_response(user_input):
    intent = predict_intent(user_input)
    return get_response(intent)

# --------------------------------------------------
# TERMINAL CHAT (RUN BOT)
# --------------------------------------------------
if __name__ == "__main__":
    print("🤖 Chatbot is running (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bot: Goodbye 👋")
            break
        print("Bot:", chat_response(user_input))
