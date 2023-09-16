# Speech-Recognition

**Speech Recognition Chatbot**

This is a simple Python script that uses the speech_recognition library to create a basic chatbot that can recognize and respond to spoken commands.

**Dependencies**
speech_recognition: A library for performing speech recognition, which in this case, utilizes the Google Web Speech API.
Usage
Make sure you have the necessary dependencies installed by running:

Code:- 
pip install speech_recognition
Run the chatbot.py script.

The chatbot will listen for audio input through your microphone. Simply speak a command or question.

The chatbot will process the audio and respond accordingly.

Commands
what is your name: Chatbot introduces itself.
how are you: Chatbot responds with a polite message about its well-being.
hi: Standard greeting.
bye: Standard farewell message.
tell me a joke: Chatbot tells a pre-programmed joke.
who created you: Chatbot reveals its creator.
help: Chatbot provides information on what it can do.
what is the weather like today: Indicates that it doesn't have access to real-time weather information.
can you sing a song: Informs that it can't sing, but it's good at chatting.
Adding More Responses
To expand the chatbot's capabilities, you can add more user inputs and corresponding responses in the generate_response function.

Code:- 

# Add more user inputs and responses here
responses = {
    "new user input": "Corresponding response",
    ...
}
Please note that this is a basic template and you may want to customize it further based on your specific use case or any additional features you implement in the future.

Video file and its explain:
https://github.com/meshramkajal/Speech-Recognition/assets/131768929/48a368a1-ba01-48b1-b1a6-65957338fda0





