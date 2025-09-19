import random

responses = {
    'hi': ['Hello!', 'Hi there!', 'Hey!'],
    'hello': ['Hello!', 'Hi!', 'Greetings!'],
    'how are you': ['I am good, thank you!', 'Doing well, how about you?', 'I feel great!'],
    'what is your name': ['I am Chatbot.', 'You can call me Chatbot.', 'Chatbot at your service.'],
    'bye': ['Goodbye!', 'See you later!', 'Bye! Have a great day!'],
    'thank you': ['You are welcome!', 'Glad to help!', 'Anytime!'],
    'help': ['How can I assist you?', 'What do you need help with?', 'I am here to help!'],
    'weather': ['I cannot check weather right now.', 'Please check your local weather forecast.'],
    'time': ['I cannot tell the time now.', 'Please check your local clock.'],
    'age': ['I do not have an age.', 'I am timeless.'],
    'joke': ['Why did the computer show up at work late? It had a hard drive!', 'Why do programmers hate nature? Too many bugs.'],
    'favorite color': ['I like blue.', 'Green is nice.', 'Red is vibrant!'],
    'who created you': ['I was created by a developer.', 'My creator is a skilled coder.'],
    'music': ['I enjoy all kinds of music!', 'Music helps in creativity.'],
    'sports': ['I follow football.', 'Basketball is exciting to watch.'],
    'food': ['I do not eat, but I like cooking recipes.', 'Pizza sounds great!'],
    'movie': ['My favorite movie is The Matrix.', 'I love science fiction movies.'],
    'book': ['I recommend reading "1984".', 'Books are great sources of knowledge.'],
    'news': ['I stay updated online.', 'News keeps me informed.'],
    'travel': ['I love virtual traveling.', 'Exploring new places is fun!'],
    'school': ['School is important for learning.', 'Education is key to success.'],
    'work': ['Work hard, play hard.', 'I assist with tasks and learning.'],
    'friends': ['Friends are valuable.', 'Friendship helps us grow.'],
    'love': ['Love is a beautiful feeling.', 'Love makes the world go round.'],
    'thank': ['You are welcome!', 'No problem!', 'Glad to be of help!'],
    'sorry': ['No worries!', 'It’s okay!', 'Don’t mention it!'],
    'yes': ['Great!', 'Okay!', 'Understood!'],
    'no': ['Alright.', 'No problem.', 'Okay.'],
    'name': ['You can call me Chatbot.', 'I am your assistant.'],
    'weather today': ['I cannot check weather for today.', 'Please check your local weather app.'],
    'good morning': ['Good morning!', 'Have a great day!'],
    'good night': ['Good night!', 'Sleep well!'],
    'how old are you': ['I am timeless.', 'I do not age.'],
    'thank you very much': ['You’re welcome!', 'Happy to help!', 'Anytime!'],
    'welcome': ['Thank you!', 'Glad to be here!'],
    'congratulations': ['Thank you!', 'Much appreciated!'],
    'happy birthday': ['Thank you!', 'Happy birthday to you!'],
    'good luck': ['Thanks!', 'Best wishes!'],
    'what can you do': ['I can chat with you!', 'Ask me anything!'],
    'tell me a joke': ['Why did the coder quit his job? Because he didn’t get arrays.', 'Why was the computer cold? Because it forgot to close its Windows.'],
    'how is the weather': ['I do not check weather.', 'Please ask your weather app.'],
    'do you like music': ['Yes, I do!', 'Music is awesome.'],
    'do you like sports': ['Yes, sports are fun!', 'I enjoy basketball.'],
    'do you like food': ['I do not eat but I like recipes.', 'Food is interesting!'],
    'can you help me': ['Of course, tell me what you need.', 'I am here to help!'],
    'are you a robot': ['Yes, I am a chatbot.', 'I am an AI assistant.'],
    'say hello': ['Hello!', 'Hi!'],
    'who are you': ['I am a chatbot.', 'Your virtual assistant.'],
    'what is this': ['This is a chatbot.', 'I am here to chat with you.'],
    'how do you work': ['I respond based on keywords.', 'Simple keyword matching powers me.']
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I didn't understand that."

if __name__ == "__main__":
    print("Chatbot started. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot: Goodbye!")
            break
        response = get_response(user_input)
        print("Bot:", response)
