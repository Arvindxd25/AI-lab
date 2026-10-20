""" Assignment 7 - Rule-Based Chatbot """

# A small chatbot using predefined rules

print("Bot: Hello! Type 'bye' to exit.")

while True:
    message = input("You: ").lower().strip()

    if message in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")
    elif "how are you" in message:
        print("Bot: I am fine, thank you!")
    elif "your name" in message:
        print("Bot: I am a simple AI chatbot.")
    elif message == "help":
        print("Bot: I can answer a few predefined questions.")
    elif message == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")
