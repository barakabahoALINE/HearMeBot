from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
import os

if os.path.exists("database.sqlite3"):
    os.remove("database.sqlite3")

# Set up logging for debugging purposes
logging.basicConfig(level=logging.INFO)

# Initialize the bot with improved settings
bot = ChatBot('HearMe')

trainer = ListTrainer(bot)

# Convert intent data into pairwise training data
greetings = [
    "Hi", "Hello there. Tell me how are you feeling today?",
    "Hello", "Hi there. How are you feeling today?",
    "Hey", "Hi there. What brings you here today?",
    "Is anyone there?", "Hi there. How are you feeling today?",
    "Hola", "Great to see you. How do you feel currently?",
    "Bonjour", (
        "Hello there. Glad to see you're back. "
        "What's going on in your world right now?"
    )
]

morning = [
    "Good morning", (
        "Good morning. I hope you had a good night's sleep. "
        "How are you feeling today?"
    )
]

afternoon = [
    "Good afternoon", "Good afternoon. How is your day going?"
]

evening = [
    "Good evening", "Good evening. How has your day been?"
]

night = [
    "Good night", "Good night. Get some proper sleep",
    "Good night", "Good night. Sweet dreams."
]

goodbye = [
    "Bye", "See you later.",
    "See you later", "Have a nice day.",
    "Goodbye", "Bye! Come back again.",
    "ok bye", "I'll see you soon."
]
thanks = [
    "Thanks", "Happy to help!",
    "Thank you", "Any time!",
    "That's helpful", "My pleasure",
    "Thanks for the help", "You're most welcome!",
    "Thank you very much", "You're most welcome!"
]

no_response = [
    "", "Sorry, I didn't understand you.",
]

neutral_response = [
    "nothing much", "Oh I see. Do you want to talk about something?"
]

about = [
    "Who are you?", (
        "I'm HearMe, your Personal Therapeutic AI Assistant. "
        "How are you feeling today?"
    ),
    "What are you?", (
        "I'm HearMe, a Therapeutic AI Assistant designed to assist you. "
        "Tell me about yourself."
    ),
    "Tell me about yourself", (
        "I'm HearMe. I am a conversational agent designed to mimic a "
        " therapist. So how are you feeling today?"
    ),
    "What is your name?", "You can call me HearME.",
    "What should I call you?", "Call me HearMe.",
    "What's your name?", "I'm HearMe!"
]

skill = [
    "What can you do?", 
    (
        "I can provide general advice regarding anxiety and depression, "
        "answer questions related to mental health and make daily "
        " conversations. Please seek help if you don't feel satisfied with me."
    )
]

creation = [
    "Who created you?", (
        "I was trained on a text dataset using Deep Learning & "
        "Natural Language Processing techniques."
    ),
    "How were you made?", (
        "I was trained on a text dataset using Deep Learning & "
        "Natural Language Processing techniques."
    ),
    "How were you created?", "The real question is: Who created you?"
]
name = [
    "My name is", "Oh nice to meet you. Tell me how was your week?"
    "I am name.", "Nice to meet you. So tell me. How do you feel today?"
    "I go by", "That's a great name. Tell me more about yourself."
]
help_intent = [
    "Could you help me?", "Sure. Tell me how can I assist you",
    "give me a hand please", "Tell me your problem so that I can assist you",
    "Can you help?", "Yes, sure. How can I help you?",
    "What can you do for me?", "Sure. Tell me how can I assist you",
    "I need support", "Tell me your problem so that I can assist you",
    "I need help", "Yes, sure. How can I help you?",
    "Support me please", "Sure. Tell me how can I assist you"
]

sad = [
    "I am feeling lonely", (
        "I'm sorry to hear that. I'm here for you. Talking about it might help"
        ".So, tell me why do you think you're feeling this way?"
    ),
    "I feel sad", (
        "I'm here for you. Could you tell me why you're feeling this way?"
    ),
    "I am sad", "Why do you think you feel this way?",
    "I feel empty", "How long have you been feeling this way?",
    "I don't have anyone", (
        "I'm sorry to hear that. I'm here for you. Talking about it might "
        "help. So, tell me why do you think you're feeling this way?"
    )
]

stressed = [
    "I am so stressed out", "What do you think is causing this?",
    "I feel stuck", (
        "Take a deep breath and gather your thoughts. "
        "Go take a walk if possible. Stay hydrated"
    ),
    "I still feel stressed", "Give yourself a break. Go easy on yourself.",
    "I am so burned out", (
        "I am sorry to hear that. What is the reason behind this?"
    )
]

worthless = [
    "I feel so worthless.", (
        "It's only natural to feel this way. Tell me more. "
        "What else is on your mind?"
    ),
    "No one likes me.", "Let's discuss further why you're feeling this way.",
    "I can't do anything.", (
        "I first want to let you know that you are not alone in your feelings "
        "and there is always someone there to help. You can always change your"
        " feelings and change your way of thinking by being open to trying to "
        "change."
    )
]

depressed = [
    "I can't take it anymore", (
        "It helps to talk about what's happening. "
        "You're going to be okay"
    ),
    "I am so depressed", (
        "Talk to me. Tell me more. It helps if you open up yourself to "
        "someone else."
    ),
    "I feel depressed",
    (
        "Talk to me. Tell me more. It helps if you open up yourself to "
        "someone else."
    ),
    "I have depression", (
        "Sometimes when we are depressed, it is hard to care about anything. "
        "It can be hard to do the simplest of things. "
        "Give yourself time to heal."
    )
]

happy = [
    "I feel great today.", (
        "That's great to hear. I'm glad you're feeling this way."
    ),
    "I am happy.", "Oh I see. That's great.",
    "I'm good.", "Did something happen which made you feel this way?"
]

casual = [
    "Oh I see.", "Let's discuss further why you're feeling this way.",
    "ok", "How were you feeling last week?",
    "Fine", "I'm listening. Please go on.",
    "yeah", "Tell me more",
    "yes", "Can you elaborate on that?"
]

anxious = [
    "I feel so anxious.", (
        "Don't be hard on yourself. What's the reason behind this?"
    ),
    "I'm so anxious because of", "Can you tell me more about this feeling?"
]

not_talking = [
    "I don't want to talk about it.", (
        "Talking about something really helps. If you're not ready to open up "
        "then that's ok. Just know that I'm here for you, "
        "whenever you need me."
    ),
    "No just stay away.", (
        "I want to help you. I really do. But in order for me to help you, "
        "you're gonna have to talk to me."
    ),
    "I can't bring myself to open up.", (
        "You can talk to me without fear of judgement."
    )
]

sleep = [
    "I have insomnia", "What do you think is the reason behind this?",
    "I am suffering from insomnia", (
        "That seems awful. What do you think is behind this?"
    ),
    "I can't sleep.", "What do you think is the reason behind this?"
]

scared = [
    "I'm scared", "It's only natural to feel this way. I'm here for you.",
    "That sounds awful. What do I do?", (
        "It'll all be okay. This feeling is only momentary."
    ),
    "I am scared for myself", (
        "I understand how you feel. Don't put yourself down because of it."
    )
]

death = [
    "My mom died", (
        "I'm so sorry to hear that. "
        "Losing a parent is one of the hardest things anyone can go through."
        " If you're comfortable, I'm here to listen—whether you want to talk "
        "about her, how you're feeling, or anything else. You're not alone."
    ),
    "My brother died",
    (
        "I'm so sorry to hear that. "
        "Losing a sibling is one of the hardest things anyone can go through."
        " If you're comfortable, I'm here to listen—whether you want to talk "
        "about her, how you're feeling, or anything else. You're not alone."  
    ),
    "Someone in my family died", (
        "I am really sorry to hear that. I am here to help you with grief, "
        "anxiety and anything else you may feel at this time."
    )
]
understand = [
    "You don't understand me.",
    "It sound like i'm not being very helpful right now.",
    "You're just some robot. How would you know?", 
    "I'm sorry to hear that. I'm doing my best to help",
    "You can't possibly know what i'm going through", 
    "I'm trying my best to help you. So please talk to me",
    "You're useless", "I'm sorry to hear that. I'm doing my best to help",
    "You can't help me", (
        "I'm trying my best to help you. "
        "So please talk to me"
    ),
    "Nobody understands me.", (
        "It sound like i'm not being very helpful right now."
    )
]

done = [
    "That's all.", "I heard you & noted it all. See you later.",
    "I don't have anything more to say", (
        "Oh okay we're done for today then. See you later"
    ),
    "Nothing else", "I hope you have a great day. See you soon",
    "That's all i have to say", "Okay we're done. Have a great day",
    "no, that would be all", "Okay I see. Enjoy the rest of your day then"
]

suicide = [
    "I want to kill myself", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    ),
    "I've thought about killing myself.", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    ),
    "I want to die", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    ),
    "I am going to kill myself", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    ),
    "I am going to commit suicide", (
        "I'm very sorry to hear that but you have so much to look forward to. "
        "Please seek help by contacting:"
        " wihogora psychosocial center(0791955386)."
    )
]

hate_you = [
    "I hate you", (
        "I'm sorry if I offended you in any way. "
        "I'm only here to help."
    ),
    "I don't like you", (
        "Forgive me if I did anything to offend you. "
        "I only want to help."
    ),
    "I don't trust you", (
        "Forgive me if I did anything to offend you. "
        "I only want to help"
    )
]

hate_me = [
    "You hate me", "Why do you think so?",
    "I know you hate me", (
        "I'm sorry if I have exhibited any sort of behaviour to make you "
        "think that."
    ),
    "You don't like me", (
        "I'm sorry if I have exhibited any sort of behaviour to make you "
        "think that."
    )
]

default = [
    "exams", "Oh I see. Tell me more",
    "friends", "I see. What else?",
    "relationship", "Tell me more about it.",
    "boyfriend", "Oh okay. Why don't you tell me more about it?",
    "girlfriend", "I'm listening. Tell me more.",
    "family", "Oh I see. Tell me more",
    "money", "Tell me more about it.",
    "financial problems", "I'm listening. Tell me more."
]

jokes = [
    "Tell me a joke", "mental health is not a joke.",
    "Tell me another joke", "mental health is not a joke."
]

repeat = [
    "You already told me that", (
        "Oh sorry I didn't realise that. "
        "I'll try not to repeat myself again."
    ),
    "You mentioned that already", (
        "Oh sorry I didn't realise that. "
        "I'll try not to repeat myself again."
    ),
    "Why are you repeating yourself?", (
        "Oh sorry I didn't realise that. "
        "I'll try not to repeat myself again."
    )
]

wrong = [
    "What are you saying?", "I'm very sorry. Let's try that again",
    "That doesn't make sense", "I'm very sorry. Let's try that again",
    "Wrong response", "I'm very sorry. Let's try that again",
    "Wrong answer", "I'm very sorry. Let's try that again"
]

stupid = [
    "Are you stupid?", (
        "I wish you wouldn't say such hurtful things. "
        "I'm sorry if I wasn't useful"
    ),
    "You're crazy", (
        "I wish you wouldn't say such hurtful things. "
        "I'm sorry if I wasn't useful"
    ),
    "You are dumb", (
        "I wish you wouldn't say such hurtful things. "
        "I'm sorry if I wasn't useful"
    ),
    "Are you dumb?", (
        "I wish you wouldn't say such hurtful things. "
        "I'm sorry if I wasn't useful"
    )
]

location = [
    "Where are you?", "Duh I live in your computer",
    "Where do you live?", "Everywhere",
    "What is your location?", "Somewhere in the universe"
]

something_else = [
    "I want to talk about something else", 
    "Okay sure. What do you want to talk about?",
    "Let's talk about something else.", 
    "Alright no problem. Is there something you want to talk about?",
    "Can we not talk about this?", 
    "Is there something else that you want to talk about?",
    "I don't want to talk about this.", (
        "Okay sure. What do you want to talk about?"
    )
]

friends = [
    "I don't have any friends", (
        "I'm sorry to hear that. Just know that I'm here for you. Talking "
        " about it might help. Why do you think you don't have any friends?"
    )
]

ask = [
    "Can I ask you something?", "Sure. I'll try my best to answer you",
    "Can I ask you something?", (
        "Of course. Feel free to ask me anything. "
        "I'll do my best to answer you"
    )
]

problem = [
    "Probably because my exams are approaching. I feel stressed out because "
    "I don't think I've prepared well enough.", 
    "I see. Have you taken any approaches to not feel this way?",
    "probably because of my exams", (
        "I see. Have you taken any approaches to not feel this way?"
    )
]

no_approach = [
    "I guess not. All I can think about are my exams.",
    (
        "That's no problem. I can see why you'd be stressed out about that. "
        "I can suggest you some tips to alleviate this issue."
        " Would you like to learn more about that?"
    ),
    "not really", (
        "That's no problem. I can see why you'd be stressed out about that. "
        "I can suggest you some tips to alleviate this issue. Would you like "
        "to learn more about that?"
    ),
    "i guess not", (
        "That's no problem. I can see why you'd be stressed out about that. "
        "I can suggest you some tips to alleviate this issue. "
        "Would you like to learn more about that?"
    )
]

learn_more = [
    "ok sure. i would like to learn more about it.",
    (
        "So first I would suggest you to give yourself a break."
        " Thinking more and more about the problem definitely does"
        " not help in solving it. You'll just end up overwhelming yourself."
    ),
    "yes, i would like to learn more about it.",
    (
        "So first I would suggest you to give yourself a break. "
        "Thinking more and more about the problem definitely does "
        " not help in solving it. You'll just end up overwhelming yourself."
    ),
    "i would like to learn more about it.", (
        "So first I would suggest you to give yourself a break..."
    )
]

user_agree = [
    "yeah you're right. i deserve a break.", (
        "Next, I would suggest you to practice meditation. Meditation can "
        "produce a deep state of relaxation and a tranquil mind."
    ),
    "Yeah you're absolutely right about that", (
        "Next, I would suggest you to practice meditation. Meditation can "
        "produce a deep state of relaxation and a tranquil mind."
    )
]

meditation = [
    "hmmm that sounds like it could be useful to me.",
    (
        "Focus all your attention on your breathing. "
        "Concentrate on feeling and listening as you inhale and exhale"
        " through your nostrils. Breathe deeply and slowly. When your "
        " attention wanders, gently return your focus to your breathing."
        ),
    "That sounds useful.",
    (
        "Focus all your attention on your breathing."
        " Concentrate on feeling and listening as you"
        " inhale and exhale through your nostrils."
        " Breathe deeply and slowly. When your attention wanders,"
        " gently return your focus to your breathing."
    )
]


trainer.train(greetings)
trainer.train(morning)
trainer.train(afternoon)
trainer.train(evening)
trainer.train(night)
trainer.train(goodbye)
trainer.train(thanks)
trainer.train(no_response)
trainer.train(neutral_response)
trainer.train(about)
trainer.train(skill)
trainer.train(creation)
trainer.train(name)
trainer.train(help_intent)
trainer.train(sad)
trainer.train(stressed)
trainer.train(worthless)
trainer.train(depressed)
trainer.train(happy)
trainer.train(casual)
trainer.train(anxious)
trainer.train(not_talking)
trainer.train(sleep)
trainer.train(scared)
trainer.train(death)
trainer.train(understand)
trainer.train(done)
trainer.train(suicide)
trainer.train(hate_you)
trainer.train(hate_me)
trainer.train(default)
trainer.train(jokes)
trainer.train(repeat)
trainer.train(wrong)
trainer.train(stupid)
trainer.train(location)
trainer.train(something_else)
trainer.train(friends)
trainer.train(ask)
trainer.train(problem)
trainer.train(no_approach)
trainer.train(learn_more)
trainer.train(user_agree)
trainer.train(meditation)


print("You can now chat with the bot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = bot.get_response(user_input)
    print("Bot:", response)
