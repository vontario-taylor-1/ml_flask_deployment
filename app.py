import time
import streamlit as st
from fuzzywuzzy import process
from data import data  # Importing the predefined dataset


# Function to find the most relevant answer


# Just using hardcoded data
def get_answer_primitive(user_input):
    if not user_input.strip():
        st.write("Please enter a question.")
    else:
        user_input = user_input.lower()
        for entry in data:
            if entry["question"].lower() in user_input:
                return entry["answer"]
    return "I'm sorry, I don't have the information you're looking for. Please contact our support team for further assistance."


# Function to find the most relevant answer using fuzzy matching
def get_answer(user_input):
    # Extract questions from the dataset
    questions = [entry["question"] for entry in data]

    # Get the best match using fuzzy matching
    best_match, confidence = process.extractOne(user_input, questions)

    # Set a confidence threshold to ensure relevance
    if confidence > 70:  # Confidence threshold
        for entry in data:
            if entry["question"] == best_match:
                return entry["answer"]

    return "I'm sorry, I don't have the information you're looking for. Please contact our support team for further assistance."


def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            max-width: 800px;
            margin: 0 auto;
        }
        .title {
            font-family: Arial, sans-serif;
            font-size: 32px;
            color: #31333F;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .question-input {
            margin-top: 20px;
        }
        .answer-box {
            background-color: #F8F9F8;
            border-radius: 10px;
            padding: 20px;
            font-size: 16px;
            color: #31333F;
        }
        .custom-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .custom-button:hover {
            background-color: #45a049;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )


# Streamlit App Setup with Custom Styles
add_custom_css()  # Adding custom CSS

# Streamlit App Setup
st.markdown(
    "<h1 class='title'>Thoughtful AI - Customer Support Agent</h1>",
    unsafe_allow_html=True,
)

st.write(
    "Hi! I'm here to help you with your questions about Thoughtful AI. Ask me anything about our AI agents, and I'll do my best to assist you."
)

# User Input
user_input = st.text_input(
    "Type your question here:", key="question", help="Ask about our AI agents"
)

if st.button("Submit"):
    if user_input:
        with st.spinner("Processing..."):
            time.sleep(1)
            answer = get_answer(user_input)
        st.markdown(
            f"<div class='answer-box'><strong>Answer:</strong> {answer}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter a question before submitting.")


# Display answer when user submits a question
if user_input:
    with st.spinner("Processing..."):
        time.sleep(1)  # Simulate processing delay
        answer = get_answer(user_input)
    st.markdown(
        f"<div class='answer-box'><strong>Answer:</strong> {answer}</div>",
        unsafe_allow_html=True,
    )
