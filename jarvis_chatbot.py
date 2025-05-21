import aiml
import pyttsx3

kernel = aiml.Kernel()
kernel.learn("jarvis.aiml")

engine = pyttsx3.init()

print("=== Jarvis Chatbot ===")
print("Type something. Type 'exit' to quit.\n")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = kernel.respond(user_input.upper())
    print("Jarvis:", response)
    if response:
        engine.say(response)
        engine.runAndWait()
