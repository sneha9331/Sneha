def respond(user_input):
    if any(greeting in user_input.lower() for greeting in ['hi', 'hello', 'hey']):
        return "Hello! How can I assist you with your fashion needs today?"
    elif 'best outfit for' in user_input.lower():
        return "The best outfit depends on the occasion. Can you tell me more about the event?"
    elif 'casual' in user_input.lower():
        return "How about a pair of jeans with a comfortable t-shirt or blouse?"
    elif 'formal' in user_input.lower():
        return "A formal suit or a dress would be perfect. Do you have a color preference?"
    elif 'recommend' in user_input.lower():
        return "I suggest you try something based on current trends. What type of fashion are you into?"
    else:
        return "I'm sorry, I didn't quite catch that. Could you ask me about fashion styles, trends, or outfits?"

def start_chat():
    print("FashionBot: Hi, welcome to the fashion app!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'bye', 'quit']:
            print("FashionBot: Goodbye!")
            break
        print("FashionBot:", respond(user_input))

start_chat()

import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

patterns = [
    (r"hi|hello|hey", ["Hello! How can I assist you with your fashion needs today?"]),
    (r"what is the best outfit for (.*)", ["The best outfit for %1 depends on the occasion. Can you tell me more about the event?"]),
    (r"i need something casual", ["How about a pair of jeans with a comfortable t-shirt or blouse?"]),
    (r"i need something formal", ["A formal suit or a dress would be perfect. Do you have a color preference?"]),
    (r"what do you recommend for (.*)", ["I suggest you try something for %1 based on current trends. What type of fashion are you into?"]),
    (r"(.*)", ["I'm sorry, I didn't quite catch that. Could you ask me about fashion styles, trends, or outfits?"])
]

chatbot = Chat(patterns, reflections)

def start_chat():
    print("FashionBot: Hi, welcome to the fashion app!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'bye', 'quit']:
            print("FashionBot: Goodbye!")
            break
        print("FashionBot:", chatbot.respond(user_input))

start_chat()
