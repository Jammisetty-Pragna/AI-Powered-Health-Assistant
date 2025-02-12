import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):

    if "symptom" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    elif "stomachpain" in user_input:
        return "Stomach pain can have various reasons like indigestion,gas,etc.\n 1.TAKE REST:Sit or lie down in a comfortable position to relax your abdominal muscles\n2.WARM COMPRESS:Place a heating pad or warm cloth on your stomach to ease the pain\n3.STAY HYDRATED:Sip on warm water herbal tea or clear fluids to stay hydrated and soothe your stomach"
    elif "headache" in user_input:
        return "Headache can be caused by various factors such as stress,dehydration,lack of sleep,etc..\nHere are few suggestions to help you:\n1.DRINK WATER:Dehydration is a common cause to the headache,so try sipping water./n2.TAKE A BREAK:Rest your eyes and mind\n3.APPLY A COOL COMPRESS:Place a cold cloth or an ice pack on your forehead or on back of your neck\n4.MASSAGE:Gently massage your temples,neck or the area wher you feel pain"
    elif "virus" in user_input:
        return "Tt is better to consult a doctor if you felt like that"
    else:
        response = chatbot(user_input, max_length=300, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?", "")
    
    # Display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query ,Please Wait......"):
                
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
