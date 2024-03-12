import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?",]
    ],
    [
        r"i[' ]?am good|great|fine|okay",
        ["Glad to hear that!",]
    ],
    [
        r"what (?:is|are) your name|who are you ?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"what can you do|how can you help me ?",
        ["I can provide information, answer questions, or just chat with you. Feel free to ask me anything!",]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help you. What do you need assistance with?",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual assistant and don't have a physical location. I'm here to help you wherever you are!",]
    ],
    [
        r"(.*) your name ?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"bye|goodbye|see you",
        ["Goodbye! Take care.", "Bye, have a great day!"]
    ],
]

# Create a chatbot using the defined pairs
def chatbot():
    print("Hi! I'm ChatBot. How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

# Call the chatbot function to start the conversation
if __name__ == "__main__":
    chatbot()
