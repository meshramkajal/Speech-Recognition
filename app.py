import speech_recognition as sr
import random

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_to_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def process_audio(audio):
    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        return text.lower()  # Convert to lowercase for easier matching
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, there was an issue connecting to the Google Web Speech API."

def generate_response(user_input):
    responses = {
        "what is your name": "My name is Kajal.",
        "how are you": "I'm doing well, thank you!",
        "hi": "Hello there!",
        "bye": "Goodbye! Take care.",
        "tell me a joke": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
        "who created you": "I was created by bot.",
        "help": "I can answer questions, tell jokes, and have general conversations. Just ask me anything!",
        "what is the weather like today": "I'm sorry, I don't have access to real-time information.",
        "can you sing a song": "I'm afraid I can't sing, but I'm great at chatting!",
        # Add more user inputs and responses here
    }
    
    # Look up the response based on user input
    response = responses.get(user_input, None)
    
    if response is None:
        response = random.choice([
            "Interesting question! Could you please provide more details?",
            "I'm not sure, but I'm here to learn with you.",
            "Let's explore that together! What do you think?",
        ])
        
    return response

# Main loop
while True:
    audio_input = listen_to_audio()
    user_input = process_audio(audio_input)
    print("User:", user_input)
    
    response = generate_response(user_input)
    print("Chatbot:", response)
