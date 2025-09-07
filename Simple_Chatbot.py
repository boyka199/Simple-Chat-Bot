#creating own chatbot
#reflection(response: 1: pattern 2:respond)
import nltk
from nltk.chat.util import Chat, reflections

#Define a set of patterns and responses a=[(r'user's question',[chat bot's answer])]
patterns =[
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'what is your name?', ['I am a chatbot. You can call me ChatGPT.']),
    (r'how are you?', ['I am doing well, thank you!', 'I am fine, thanks for asking!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
    (r'tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!']),
    (r'(.*)', ['I am sorry, I did not understand that.', 'Could you please rephrase that?']),
    (r'(.*) age', ['I dont have an age.'])
]

#create a chatbot using the patterns

chatbot = Chat(patterns, reflections)

#function to start the conversation
def start_chatbot():
  print('Hello! I am a chatbot. How can I help you today?')
  while True:
      user_input = input('You: ')
      if user_input.lower() == 'exit':
          print('Goodbye!')
          break
      response = chatbot.respond(user_input)
      print('Chatbot:', response)

#start the chat
start_chatbot()