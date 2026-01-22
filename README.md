# 🤖 AI-Powered Conversational Chatbot

An intelligent AI-powered chatbot built using Python, Natural Language Processing (NLP), and Deep Learning. This project demonstrates an end-to-end AI application pipeline, including text preprocessing, intent classification using a neural network, backend integration with Flask, and a web-based user interface.

---

## 📌 Project Overview

This chatbot is an intent-based conversational system designed to understand user messages and respond appropriately. It uses NLP techniques for text processing and a Deep Learning model for intent classification, making it suitable for demonstrating practical AI and Deep Learning skills in internship and entry-level roles.

---

## 🧠 Key Features

- Intent classification using Deep Learning
- NLP preprocessing (tokenization and lemmatization)
- Bag-of-Words feature representation
- Flask-based backend for real-time inference
- Web-based chat interface
- Keyboard support (Enter key to send messages)
- Modular and scalable project structure

---

## 🏗️ Project Structure

ai_chatbot/
├── app/
│ ├── app.py
│ ├── chatbot_logic.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── style.css
├── data/
│ └── intents.json
├── model/
│ └── chatbot_model.keras
├── notebooks/
│ └── training.ipynb
├── requirements.txt
└── README.md


---

## ⚙️ Tech Stack

- Python
- Natural Language Processing (NLTK)
- Deep Learning (TensorFlow / Keras)
- Flask
- HTML, CSS, JavaScript

---

## 🔍 How It Works

1. User enters a message in the web interface  
2. Text is preprocessed using NLP techniques  
3. Input is converted into a Bag-of-Words vector  
4. A Deep Learning model predicts the user intent  
5. A suitable response is selected and displayed  

---

## 🚀 Running the Project Locally

### 1. Clone the Repository
bash
git clone https://github.com/your-username/ai-powered-chatbot.git
cd ai-powered-chatbot


### 2. Create and Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Download Required NLTK Data
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

### 5. Run the Flask Application
python app/app.py

### 6. Open in Browser
http://127.0.0.1:5000/

## 💬 Sample Interactions
User Input	Bot Response
Hi	Hello! How can I help you today?
Thanks	You're welcome!
Bye	Goodbye! Take care!

## 📈 Learning Outcomes

Implemented NLP preprocessing pipelines

Built and trained a Deep Learning model for intent classification

Integrated AI models with a Flask backend

Developed a user-friendly web-based chatbot interface

Gained experience debugging and structuring AI applications

🔮 Future Enhancements

Add fallback responses for unknown queries

Improve intent confidence handling

Add conversational context and memory

Deploy backend on cloud platforms

## 👤 Author

Aditya Ghate
B.Tech CSE (AI & ML)

## ⭐ Acknowledgements

TensorFlow & Keras Documentation

NLTK Library

Open-source NLP community
